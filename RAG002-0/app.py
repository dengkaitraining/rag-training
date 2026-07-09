"""
# Program:
#       RAG Example - User Prompt.
# History:
# 2026/07/09	Kyle	First release
1. import ubprocess, os, json, markdown, requests, load_dotenv
2. 
"""
from flask import Flask, request, render_template
import subprocess, os, json, markdown, requests  
from dotenv import load_dotenv

"""
# Function: run_requests_function
# Description:
#       This function sends a POST request to the Gemini API using the requests library.
#       It retrieves the API key and URL from environment variables, prepares the JSON payload,
#       sets the necessary HTTP headers, and handles any exceptions that may occur during the request.
# Parameters:
#       user_prompt (str): The user input that will be sent to the Gemini API.
# Returns:
#       response (requests.Response or str): The response from the Gemini API, or an error message in case of an exception.
# Usage:
#       response = run_requests_function(user_prompt)
# History:
# 2026/07/09	Kyle	First release
#
"""
def run_requests_function(user_prompt):  
    # 載入同目錄下的 .env 檔案
    load_dotenv()

    # 讀取特定環境變數
    #api_key = os.getenv("kyle_api_key", "")
    api_key = os.getenv("training_api_key", "")
    #api_key = os.getenv("innovation_api_key", "")
    
    # 讀取 Gemini API URL
    url = os.getenv("gemini_api_url", "")

    # 準備要傳送的 JSON 資料，將 user_prompt 放入
    transfer_data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_prompt
                    }
                ]
            }
        ]
    }

    # 設定 HTTP 標頭，包含 Content-Type 和 API Key
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": api_key
    }

    if not url or not api_key:
        raise ValueError("Gemini API URL or API Key is not set in the environment variables.")

    rc_text = ""
    try:
        # 使用 requests.post() 發送 POST 請求，並取得回應
        response = requests.post(
            url,
            json=transfer_data,
            headers=headers
        )
        # response.raise_for_status()  # 如果回應狀態碼不是 200，會拋出 HTTPError
        rc_text = response.text
    except requests.exceptions.RequestException as e:
        # 捕捉所有 requests 相關的例外，並回傳錯誤訊息
        response = json.dumps({"error": str(e)})
        rc_text = ""
    
    return rc_text

"""
# Function: string_to_json
# Description:
#       This function attempts to convert a string to a JSON object.
#       If the string is not valid JSON, it returns a dictionary with an error message.
# Parameters:
#       string (str): The string to be converted to JSON.
# Returns:
#       dict: A JSON object if the conversion is successful, or an error message if it fails.
# Usage:
#       json_data = string_to_json(string)
# History:
# 2026/07/09	Kyle	First release
#
"""
def string_to_json(string):
    try:
        return json.loads(string)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}

app = Flask(__name__)

"""
# Function: markdown_to_html
# Description:
#       This function converts Markdown text to HTML.
#       It uses the markdown library with 'extra' and 'codehilite' extensions for enhanced Markdown features and syntax highlighting.
# Parameters:
#       markdown_text (str): The Markdown text to be converted to HTML.
# Returns:
#       str: The converted HTML text.
# Usage:
#       html_text = markdown_to_html(markdown_text)
# History:
# 2026/07/09	Kyle	First release
#
"""
def markdown_to_html(markdown_text):
    # 將 Markdown 轉換為 HTML
    # 這裡可以使用第三方套件如 markdown2 或 mistune 來進行轉換
    # 這裡僅示範簡單的替換，實際應用中建議使用專門的 Markdown 解析器
    #html_text = markdown_text.replace("\n", "<br>")
    
    html_text = markdown.markdown(markdown_text, extensions=['extra', 'codehilite'])
    return html_text

@app.route('/')
def index():
    # 使用 send_static_file() 回傳靜態網頁 index.html
    return app.send_static_file('index.html')

@app.route('/process', methods=['POST'])
def process():
    # 從 POST 請求中取得 user_prompt 欄位資料
    user_prompt = request.form.get('user_prompt', '')
    # 向 LLM API 發送請求，並取得回應結果，傳送到 output.html
    llm_text = run_requests_function(user_prompt)
    
    #result = run_requests_function(user_prompt)
    #data = string_to_json(result)

    #llm_text = data["candidates"][0]["content"]["parts"][0]["text"]

    # 將 LLM 回應的 Markdown 轉換為 HTML
    #llm_text = markdown_to_html(llm_text)

    # 渲染 dynamic/template 網頁 output.html，並將 user_prompt 帶入
    return render_template('output.html', user_prompt=user_prompt, llm_response=llm_text)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)

