#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新嗷呜配置（仅更新相同 key 的站点 + 本地化 spider）
- 获取最新嗷呜配置
- 只更新现有配置中 key 相同的站点
- 下载 spider 图片并保存为 aw1.png，更新配置为本地路径
- 不新增、不删除任何站点
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
CONFIG_FILE = Path("aowu测试.json")
LOCAL_SPIDER_PATH = "./jar/aw1.png"  # ★★★ 改为 aw1.png ★★★
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

def merge_by_key(existing, new):
    """只更新相同 key 的站点（直接修改 existing）"""
    if not isinstance(existing, dict) or not isinstance(new, dict):
        return existing
    
    if "sites" in existing and "sites" in new:
        existing_sites = existing["sites"]
        new_sites_dict = {site.get("key"): site for site in new["sites"] if "key" in site}
        
        for i, old_site in enumerate(existing_sites):
            old_key = old_site.get("key")
            if old_key and old_key in new_sites_dict:
                print(f"🔄 更新站点: {old_key}")
                existing_sites[i] = deep_merge(old_site, new_sites_dict[old_key])
            else:
                print(f"⏭️ 保留站点（嗷呜无对应）: {old_key}")
    
    return existing

def extract_spider_url(config):
    """提取 spider 字段中的有效 URL"""
    spider_raw = config.get("spider", "")
    if not spider_raw:
        return None
    
    if ";" in spider_raw:
        clean_url = spider_raw.split(";")[0]
    else:
        clean_url = spider_raw
    
    clean_url = clean_url.strip()
    
    if clean_url.startswith("http://") or clean_url.startswith("https://"):
        return clean_url
    else:
        return None

def download_and_localize_spider(config):
    """
    下载 spider 图片并保存为 aw1.png，替换配置中的 spider 路径
    """
    remote_url = extract_spider_url(config)
    if not remote_url:
        print("ℹ️ 未检测到有效的远程 spider 链接，跳过下载")
        return False
    
    print(f"🔗 检测到远程 spider: {remote_url}")
    
    try:
        JAR_DIR.mkdir(exist_ok=True)
        save_path = JAR_DIR / "aw1.png"  # ★★★ 保存为 aw1.png ★★★
        print(f"⬇️ 正在下载 spider 图片...")
        response = requests.get(remote_url, timeout=30)
        if response.status_code != 200:
            print(f"❌ 下载失败: {response.status_code}")
            return False
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ spider 图片已保存: {save_path} ({len(response.content)} 字节)")
        
        # 将配置中的 spider 替换为本地路径
        config["spider"] = LOCAL_SPIDER_PATH
        print(f"🔄 spider 字段已更新为本地路径: {LOCAL_SPIDER_PATH}")
        return True
    except Exception as e:
        print(f"⚠️ 下载或替换失败: {e}")
        return False

def main():
    print("=" * 50)
    print("🔄 更新嗷呜配置（更新相同key + 本地化spider -> aw1.png）")
    print("=" * 50)
    
    # 1. 获取最新嗷呜配置
    new_config = fetch_decrypted_data()
    if not new_config:
        sys.exit(1)
    
    # 2. 加载现有配置
    existing = load_existing_config()
    if existing is None:
        sys.exit(1)
    
    # 3. 保存原始副本用于比较
    original = deepcopy(existing)
    
    # 4. 按 key 合并站点
    print("\n📋 开始对比更新站点...")
    merged = merge_by_key(existing, new_config)
    
    # 5. 处理 spider 字段（下载 + 本地化）
    print("\n📋 处理 spider 字段...")
    spider_updated = download_and_localize_spider(merged)
    
    # 6. 检查是否有任何变化
    config_changed = json.dumps(original, sort_keys=True) != json.dumps(merged, sort_keys=True)
    
    if config_changed or spider_updated:
        if not save_config(merged):
            sys.exit(1)
        print("✅ 配置已更新并保存")
    else:
        print("✅ 配置无变化，无需提交")
    
    print("\n✨ 更新完成！")
    print(f"📁 配置文件: {CONFIG_FILE}")
    print(f"📁 图片路径: {LOCAL_SPIDER_PATH}")
    print("=" * 50)

if __name__ == "__main__":
    main()
