# -*- coding: utf-8 -*-
"""
Flask Web Application：4x2x3 ANN 鳶尾花品種預測
=================================================

規格對應
--------
1. 輸入表單頁面是靜態頁面
   -> GET '/' 直接回傳 static/form.html（純 HTML 檔案，
      未經過 Jinja2 樣板引擎處理，內容固定不變）。

2. 呈現預測結果的頁面是動態頁面
   -> POST '/predict' 依使用者輸入的數值即時運算，
      透過 render_template 搭配 templates/result.html
      動態產生內容（每次輸入不同，頁面內容也不同）。

3. 前端不使用 CSS，也不使用 JavaScript
   -> 兩個頁面皆為純 HTML 標籤（無 <style>、無外部 css、
      無 <script>、無 on* 事件屬性）。

模型參數
--------
本程式不重新呼叫 scikit-learn 訓練，而是直接讀取先前訓練好、
儲存在 ann_params.yaml 的權重(W1, b1, W2, b2)與標準化參數
(mean, scale)，以 numpy 手動實作前向傳遞：

    x_scaled = (x - mean) / scale
    hidden   = sigmoid(x_scaled @ W1 + b1)   # 隱藏層 activation = Sigmoid
    output   = sigmoid(hidden   @ W2 + b2)   # 輸出層 activation = Sigmoid
    predicted_class = argmax(output)
"""

import os
import numpy as np
import yaml
from flask import Flask, request, render_template, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
YAML_PATH = os.path.join(BASE_DIR, "ann_params.yaml")

app = Flask(__name__)

# ----------------------------------------------------------------------
# 載入 ANN 參數 (啟動時讀取一次即可，不需每次請求都重讀)
# ----------------------------------------------------------------------
with open(YAML_PATH, "r", encoding="utf-8") as f:
    ann_params = yaml.safe_load(f)

W1 = np.array(ann_params["parameters"]["W1_input_to_hidden"]["value"])   # (4, 2)
b1 = np.array(ann_params["parameters"]["b1_hidden_bias"]["value"])       # (2,)
W2 = np.array(ann_params["parameters"]["W2_hidden_to_output"]["value"])  # (2, 3)
b2 = np.array(ann_params["parameters"]["b2_output_bias"]["value"])       # (3,)

MEAN = np.array(ann_params["preprocessing"]["mean"])   # (4,)
SCALE = np.array(ann_params["preprocessing"]["scale"])  # (4,)

CLASS_NAMES = ann_params["architecture"]["output_layer"]["class_order"]
FEATURE_NAMES = ann_params["architecture"]["input_layer"]["feature_order"]


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def predict_iris(x1, x2, x3, x4):
    """
    輸入 4 個原始特徵值，回傳 (預測類別, 各類別 sigmoid 輸出值, 隱藏層輸出值)
    """
    x = np.array([x1, x2, x3, x4], dtype=float)
    x_scaled = (x - MEAN) / SCALE

    hidden = sigmoid(x_scaled @ W1 + b1)   # 隱藏層 Sigmoid
    output = sigmoid(hidden @ W2 + b2)     # 輸出層 Sigmoid

    predicted_idx = int(np.argmax(output))
    predicted_class = CLASS_NAMES[predicted_idx]

    probs = list(zip(CLASS_NAMES, output.tolist()))
    return predicted_class, probs, hidden.tolist()


# ----------------------------------------------------------------------
# 路由 1：靜態輸入表單頁面
# ----------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    # 直接回傳靜態 HTML 檔案，內容固定不變，不經樣板引擎處理
    return send_from_directory(os.path.join(BASE_DIR, "static"), "form.html")


# ----------------------------------------------------------------------
# 路由 2：動態預測結果頁面
# ----------------------------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        x1 = float(request.form["x1"])
        x2 = float(request.form["x2"])
        x3 = float(request.form["x3"])
        x4 = float(request.form["x4"])
    except (KeyError, ValueError):
        return render_template(
            "result.html",
            error="輸入格式錯誤，請確認 x1~x4 皆已填寫且為數字。",
        )

    prediction, probs, hidden = predict_iris(x1, x2, x3, x4)

    return render_template(
        "result.html",
        error=None,
        x1=x1, x2=x2, x3=x3, x4=x4,
        prediction=prediction,
        probs=probs,
        hidden=hidden,
        feature_names=FEATURE_NAMES,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
