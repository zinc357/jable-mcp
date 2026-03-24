import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

JABLE_URL = "https://jable.tv/videos/{code}/"
DOWNLOADS_DIR = "downloads"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)

def download_by_code(code: str) -> str:
    url = JABLE_URL.format(code=code)
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.text, "html.parser")
    # 伪代码：查找真实的 m3u8 视频地址、资源名
    m3u8_url = None
    for script in soup.find_all("script"):
        if script.string and "m3u8" in script.string:
            # 简单提取 m3u8 URL
            s = script.string
            start = s.find("https://")
            if start>-1 and ".m3u8" in s:
                end = s.find(".m3u8", start)
                m3u8_url = s[start:end+5]
                break
    if not m3u8_url:
        raise RuntimeError("未能找到 m3u8 视频地址")
    fname = f"{code}.m3u8"
    fpath = os.path.join(DOWNLOADS_DIR, fname)
    # 下载 m3u8 文件
    with open(fpath, "wb") as f:
        f.write(requests.get(m3u8_url, timeout=10).content)
    # 此处可集成 ffmpeg/aria2c 下载 ts
    # ....
    return fpath
