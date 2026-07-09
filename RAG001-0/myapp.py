import os
import requests

# Linux temp set env. value : export GEMINI_API_KEY="your_api_key_here"
# Windows temp set env. value : set GEMINI_API_KEY="your_api_key_here"
API_KEY = os.getenv("GEMINI_API_KEY")
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