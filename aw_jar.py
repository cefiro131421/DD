#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新嗷呜接口的jar包（spider字段图片）
API: https://www.qiushui.vip/gj/jiemi/raw/?url=
目标仓库: https://github.com/cefiro131421/DD/tree/master/jar
"""

import os
import sys
import json
import requests
from pathlib import Path

# ============ 配置 ============
DECRYPT_API = "https://www.qiushui.vip/gj/jiemi/raw/?url="
TARGET_URL = "http://www.英格里希嗷呜.top/tv"
JAR_DIR = Path("jar")
# ==============================

def fetch_decrypted_data():
    """调用解密API获取接口数据"""
    try:
        full_url = DECRYPT_API + TARGET_URL
        print(f"📡 正在解密: {TARGET_URL}")
        response = requests.get(full_url, timeout=30)
        
        if response.status_code != 200:
            print(f"❌ API请求失败: {response.status_code}")
            return None
            
        data = response.json()
        print("✅ 数据获取成功")
        return data
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return None

def extract_spider_url(data):
    """提取spider字段的纯图片链接"""
    spider_raw = data.get("spider", "")
    if not spider_raw:
        print("❌ 未找到spider字段")
        return None
    
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
