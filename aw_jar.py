#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新嗷呜接口的jar包（spider字段图片）
API: https://bjq.catvod.site/api/decrypt
目标仓库: https://github.com/cefiro131421/DD/tree/master/jar
"""

import os
import sys
import json
import requests
from pathlib import Path

# ============ 配置 ============
DECRYPT_API = "https://bjq.catvod.site/api/decrypt"  # ← 仅修改此处
TARGET_URL = "http://www.英格里希嗷呜.top/tv"
JAR_DIR = Path("jar")
# ==============================

def fetch_decrypted_data():
    """调用解密API获取接口数据（适配新API）"""
    try:
        print(f"📡 正在解密: {TARGET_URL}")
        
        # 新API要求 POST + JSON 格式
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
        
        # 检查返回状态（新API使用 ok 字段）
        if not result.get("ok", False):
            print(f"❌ API返回错误: {result.get('msg', '未知错误')}")
            return None
        
        data = result.get("data")
        if not data:
            print("❌ API返回数据为空")
            return None
        
        # 如果 data 是字符串，尝试解析为JSON；如果是字典则直接使用
        if isinstance(data, str):
            try:
                data = json.loads(data)
                print("✅ 数据获取成功（JSON字符串解析）")
            except json.JSONDecodeError:
                print("✅ 数据获取成功（纯文本）")
        else:
            print("✅ 数据获取成功（字典）")
        
        return data
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return None

def extract_spider_url(data):
    """提取spider字段的纯图片链接"""
    # 如果 data 是字符串，尝试解析为JSON（兼容性）
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except:
            pass
    
    if isinstance(data, dict):
        spider_raw = data.get("spider", "")
    else:
        print("❌ 数据格式不是字典，无法提取spider")
        return None
    
    if not spider_raw:
        print("❌ 未找到spider字段")
        return None
    
    # 去除 ;md5;xxx 后缀
    if ";" in spider_raw:
        clean_url = spider_raw.split(";")[0]
    else:
        clean_url = spider_raw
    
    print(f"🔗 提取到图片URL: {clean_url}")
    return clean_url

def download_and_save_image(url):
    """下载图片并保存到jar目录"""
    try:
        JAR_DIR.mkdir(exist_ok=True)
        
        filename = "aw.png"
        save_path = JAR_DIR / filename
        
        print(f"⬇️ 正在下载: {filename}")
        response = requests.get(url, timeout=30)
        
        if response.status_code != 200:
            print(f"❌ 下载失败: {response.status_code}")
            return False
            
        with open(save_path, "wb") as f:
            f.write(response.content)
        
        print(f"✅ 已保存: {save_path} ({len(response.content)} 字节)")
        return True
        
    except Exception as e:
        print(f"❌ 下载错误: {e}")
        return False

def main():
    print("=" * 50)
    print("🔄 更新嗷呜接口jar包")
    print("=" * 50)
    
    data = fetch_decrypted_data()
    if not data:
        sys.exit(1)
    
    image_url = extract_spider_url(data)
    if not image_url:
        sys.exit(1)
    
    success = download_and_save_image(image_url)
    if not success:
        sys.exit(1)
    
    print("\n✨ 更新完成！")
    print(f"📁 文件位置: {JAR_DIR / 'aw.png'}")
    print("=" * 50)

if __name__ == "__main__":
    main()
