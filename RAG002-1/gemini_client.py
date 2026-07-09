import os
import json
import requests
from dotenv import load_dotenv

class GeminiClient:
    """
    Class: GeminiClient
    Description:
        A class handler to manage connection and data conversion for the Gemini API.
    """
    def __init__(self):
        # 於建構子中載入同目錄下的 .env 檔案
        load_dotenv()
        
        # 將 API Key 與 URL 封裝為私有屬性，保護敏感資訊
        #self.__api_key = os.getenv("kyle_api_key", "")
        self.__api_key = os.getenv("training_api_key", "")
        #self.__api_key = os.getenv("innovation_api_key", "")

        self.__api_url = os.getenv("gemini_api_url", "")
        
        # 初始化時先進行基本變數檢查
        if not self.__api_url or not self.__api_key:
            raise ValueError("Gemini API URL or Kyle API Key is not set in the environment variables.")

    def generate_content(self, user_prompt):
        """傳送 POST 請求至 Gemini API 並傳回原始文字回應"""
        transfer_data = {
            "contents": [
                {
                    "parts": [{"text": user_prompt}]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": self.__api_key
        }

        try:
            response = requests.post(
                self.__api_url,
                json=transfer_data,
                headers=headers
            )
            return response.text
        except requests.exceptions.RequestException as e:
            return json.dumps({"error": str(e)})

    @staticmethod
    def to_json(json_string):
        """將字串轉換為 JSON 物件"""
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}