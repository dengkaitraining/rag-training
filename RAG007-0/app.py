from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# 線性迴歸模型係數
COEF_X1 = 0.483737
COEF_X2 = 0.005835
COEF_X3 = -0.301097
INTERCEPT = 1964.672569


@app.route("/")
def index():
    """
    輸入頁面為靜態頁面，直接由 Flask 內建的 static 資料夾提供服務，
    對應檔案為 static/index.html。
    """
    return redirect("/static/index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    接收表單提交的 x1, x2, x3，計算預測值 y，
    並以動態頁面 (Jinja2 樣板) 呈現結果。
    """
    try:
        x1 = float(request.form["x1"])
        x2 = float(request.form["x2"])
        x3 = float(request.form["x3"])
    except (KeyError, ValueError):
        return "輸入格式錯誤，請輸入數字後再試一次。", 400

    y = COEF_X1 * x1 + COEF_X2 * x2 + COEF_X3 * x3 + INTERCEPT

    return render_template(
        "result.html",
        x1=x1,
        x2=x2,
        x3=x3,
        y=round(y, 4),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
