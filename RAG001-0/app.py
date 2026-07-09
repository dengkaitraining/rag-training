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
    # 將收到的 user_prompt 傳給動態網頁 output.html
    return render_template("output.html", user_prompt = user_prompt)


if __name__ == "__main__":
    app.run(debug=True)