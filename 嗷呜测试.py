#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新嗷呜配置（仅更新相同 key 的站点）
- 获取最新嗷呜配置
- 只更新现有配置中 key 相同的站点
- 不新增、不删除任何站点
- 下载 spider 图片
"""

import os
import sys
import json
import requests
from pathlib import Path
from copy import deepcopy

# ============ 配置 ============
DECRYPT_API = "https://bjq.catvod.site/api/decrypt"
TARGET_URL = "http://www.英格里希嗷呜.top/tv"
JAR_DIR = Path("jar")
CONFIG_FILE = Path("aowu测试.json")  # 您的主配置文件
# ==============================

def fetch_decrypted_data():
    """调用解密API获取接口数据"""
    try:
        print(f"📡 正在解密: {TARGET_URL}")
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36"
        }
        payload = {"url": TARGET_URL}
        response = requests.post(DECRYPT_API, json=payload, headers=headers, timeout=30)
        
        if response.status_code != 200:
            print(f"❌ API请求失败: {response.status_code}")
            return None
        
        result = response.json()
        if not result.get("ok", False):
            print(f"❌ API返回错误: {result.get('msg', '未知错误')}")
            return None
        
        data = result.get("data")
        if not data:
            print("❌ API返回数据为空")
            return None
        
        if isinstance(data, str):
            data = json.loads(data)
        
        print("✅ 获取最新嗷呜配置成功")
        return data
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return None

def load_existing_config():
    """加载现有配置"""
    if not CONFIG_FILE.exists():
        print(f"❌ 配置文件 {CONFIG_FILE} 不存在")
        return None
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
        print(f"✅ 加载现有配置成功，共 {len(config.get('sites', []))} 个站点")
        return config
    except Exception as e:
        print(f"❌ 加载现有配置失败: {e}")
        return None

def save_config(config):
    """保存配置"""
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"✅ 配置已保存: {CONFIG_FILE}")
        return True
    except Exception as e:
        print(f"❌ 保存配置失败: {e}")
        return False

def merge_by_key(existing, new):
    """
    只更新相同 key 的站点
    - 遍历现有站点的 key，在嗷呜配置中查找相同 key 的站点
    - 如果找到：更新该站点（递归合并字段）
    - 如果没找到：保留原站点不变
    """
    if not isinstance(existing, dict) or not isinstance(new, dict):
        return existing
    
    # 处理 sites 列表
    if "sites" in existing and "sites" in new:
        existing_sites = existing["sites"]
        new_sites_dict = {site.get("key"): site for site in new["sites"] if "key" in site}
        
        for i, old_site in enumerate(existing_sites):
            old_key = old_site.get("key")
            if old_key and old_key in new_sites_dict:
                # 找到相同 key 的站点，更新
                print(f"🔄 更新站点: {old_key}")
                # 递归合并
                existing_sites[i] = deep_merge(old_site, new_sites_dict[old_key])
            else:
                # 没有匹配的 key，保留原站点
                print(f"⏭️ 保留站点（嗷呜无对应）: {old_key}")
    
    return existing

def deep_merge(base, update):
    """递归深度合并两个字典"""
    if not isinstance(update, dict):
        return update
    if not isinstance(base, dict):
        return deepcopy(update)
    
    result = deepcopy(base)
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result

def extract_spider_url(config):
    """提取 spider 图片链接"""
    spider_raw = config.get("spider", "")
    if not spider_raw:
        print("⚠️ 配置中未找到 spider 字段")
        return None
    if ";" in spider_raw:
        clean_url = spider_raw.split(";")[0]
    else:
        clean_url = spider_raw
    print(f"🔗 spider图片 URL: {clean_url}")
    return clean_url

def download_spider_image(url):
    """下载 spider 图片"""
    if not url:
        return False
    try:
        JAR_DIR.mkdir(exist_ok=True)
        save_path = JAR_DIR / "aw.png"
        print(f"⬇️ 正在下载 spider 图片...")
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            print(f"❌ 下载失败: {response.status_code}")
            return False
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ spider 图片已保存: {save_path} ({len(response.content)} 字节)")
        return True
    except Exception as e:
        print(f"❌ 下载错误: {e}")
        return False

def main():
    print("=" * 50)
    print("🔄 更新嗷呜配置（仅更新相同key的站点）")
    print("=" * 50)
    
    # 1. 获取最新嗷呜配置
    new_config = fetch_decrypted_data()
    if not new_config:
        sys.exit(1)
    
    # 2. 加载现有配置
    existing = load_existing_config()
    if existing is None:
        sys.exit(1)
    
    # 3. 按 key 合并
    print("\n📋 开始对比更新...")
    merged = merge_by_key(existing, new_config)
    
    # 4. 检查是否有变化
    if json.dumps(existing, sort_keys=True) == json.dumps(merged, sort_keys=True):
        print("✅ 配置无变化，无需提交")
    else:
        if not save_config(merged):
            sys.exit(1)
    
    # 5. 下载 spider 图片
    spider_url = extract_spider_url(merged)
    if spider_url:
        download_spider_image(spider_url)
    
    print("\n✨ 更新完成！")
    print(f"📁 配置文件: {CONFIG_FILE}")
    print("=" * 50)

if __name__ == "__main__":
    main()
