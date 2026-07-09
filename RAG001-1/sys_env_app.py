import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("找不到 GEMINI_API_KEY，請先設定環境變數")
else:
    print(f"GEMINI_API_KEY 已成功讀取: {API_KEY}")

URL = os.getenv("gemini_api_url")
if not URL:
    raise ValueError("找不到 gemini_api_url，請先設定環境變數")
else:
    print(f"gemini_api_url 已成功讀取: {URL}")