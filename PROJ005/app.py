from flask import Flask, request, render_template
# import subprocess, os
import subprocess, os, json, markdown, requests  # 新增 requests 模組的匯入
# import dotenv
from dotenv import load_dotenv

app = Flask(__name__)


# method 1. subprocess function
def run_curl_command(user_prompt):
    # 載入同目錄下的 .env 檔案
    load_dotenv()

    # 讀取特定環境變數
    kyle_api_key = os.getenv("kyle_api_key", "default_value_if_not_set")

    # Gemini Flash API 的 URL
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

    # 準備要傳送的 JSON 資料，將 user_prompt 放入
    transfer_data = f"""{{
       "contents": [
         {{
              "parts": [
             {{
               "text": "{user_prompt}"
             }}
           ]
         }}
       ]
    }}"""
    
    # 設定 curl 命令，包含 HTTP 標頭和 JSON 資料
    command = [
        "curl",
        "-X",
        "POST",
        "-H",
        "Content-Type: application/json",
        "-H",
        f"X-goog-api-key: {kyle_api_key}",
        "-d",
        transfer_data,
        url
    ]

    # 執行 curl 命令，並捕捉輸出結果
    result = subprocess.run(command, capture_output=True, text=True)
    
    # 將結果的標準輸出返回
    return result.stdout

# method 2. requests function (commented out)
def run_requests_function(user_prompt):
    # 載入同目錄下的 .env 檔案
    load_dotenv()

    # 讀取特定環境變數
    kyle_api_key = os.getenv("kyle_api_key", "default_value_if_not_set")

    # Gemini Flash API 的 URL
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
    
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
        "X-goog-api-key": kyle_api_key
    }

    # 使用 requests.post() 發送 POST 請求，並取得回應
    response = requests.post(
        url,
        json=transfer_data,
        headers=headers
    )

    # 將回應的文字內容返回
    return response.text

# String to JSON conversion function
def string_to_json(string):
    try:
        return json.loads(string)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}

# Markdown to HTML conversion function
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

    # method 1. subprocess function
    # result = run_curl_command(user_prompt)

    # method 2. requests function (commented out)
    result = run_requests_function(user_prompt)
    data = string_to_json(result)

    llm_text = data["candidates"][0]["content"]["parts"][0]["text"]

    # 將 LLM 回應的 Markdown 轉換為 HTML
    llm_text = markdown_to_html(llm_text)

    # 渲染 dynamic/template 網頁 output.html，並將 user_prompt 帶入
    return render_template('output.html', user_prompt=user_prompt, llm_response=llm_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
