from flask import Flask, request, render_template
import os
import requests

app = Flask(__name__)


@app.route("/")
def index():
    # 使用靜態網頁 index.html
    # 注意：這裡使用 app.send_static_file()
    return app.send_static_file("index.html")


@app.route("/process", methods=["POST"])
def process():
    # 從 <form> 接收 user_prompt 欄位
    user_prompt = request.form.get("user_prompt")
    # 向 LLM API發出 Request，得到回應，送到 ouput.html呈現
    
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
        raise ValueError("找不到 GEMINI_API_KEY，請先設定環境變數")

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
        "X-goog-api-key": API_KEY
    }

    # 使用 requests.post() 發送 POST 請求，並取得回應
    response = requests.post(
        url,
        json=transfer_data,
        headers=headers
    )

    # 將收到的 user_prompt 傳給動態網頁 output.html
    return render_template("output.html", user_prompt = user_prompt, response = response.text)


if __name__ == "__main__":
    app.run(debug=True)