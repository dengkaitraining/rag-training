from flask import Flask, render_template, request, jsonify
# 從自訂模組中匯入類別
from gemini_client import GeminiClient
from text_utility import TextUtility

app = Flask(__name__)

# 在全域初始化 GeminiClient，不用每次進路由都重新實例化
try:
    gemini = GeminiClient()
except ValueError as e:
    print(f"安全警告: {e}")
    gemini = None

@app.route("/")
def index():
    # return "Flask API 伺服器運作中"
    # 使用 send_static_file() 回傳靜態網頁 index.html
    return app.send_static_file('index.html')

@app.route("/process", methods=["POST"])
def process():
    if not gemini:
        return jsonify({"error": "Gemini Client 未正確初始化，請檢查環境變數。"}), 500

    # 取得前端傳來的 prompt
    #user_prompt = request.json.get("prompt", "")
    user_prompt = request.form.get('user_prompt', '')

    if not user_prompt:
        return jsonify({"error": "Prompt 不能為空"}), 400

    # 1. 呼叫 Gemini API 類別的方法
    raw_response = gemini.generate_content(user_prompt)
    
    # 2. 解析為 JSON
    response_json = GeminiClient.to_json(raw_response)
    
    # 這裡可以根據 API 回傳的格式抽取出文字，並使用 TextUtility 轉成 HTML
    # 範例：假設 response_json 中有內文，可使用 TextUtility.markdown_to_html(...)
    response_json = TextUtility.markdown_to_html((response_json["candidates"][0]["content"]["parts"][0]["text"]))

    """
    return jsonify({
        "raw_data": response_json
    })
    """

    # 渲染 dynamic/template 網頁 output.html，並將 user_prompt 帶入
    return render_template('output.html', user_prompt = user_prompt, llm_response = response_json)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 5000)