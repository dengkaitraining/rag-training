import os
import dotenv
import requests
from dotenv import load_dotenv

#API_KEY = os.getenv("GEMINI_API_KEY")

# 載入同目錄下的 .env 檔案
load_dotenv()

# 讀取特定環境變數
API_KEY = os.getenv("GEMINI_API_KEY", "")

if not API_KEY:
    raise ValueError("找不到 GEMINI_API_KEY，請先設定環境變數")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works in a few words"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())