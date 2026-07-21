# 鳶尾花品種預測 Flask App

## 目錄結構
```
iris_flask_app/
├── app.py              # Flask 主程式
├── ann_params.yaml      # 4x2x3 ANN 模型參數 (權重/偏差/標準化參數)
├── requirements.txt
├── static/
│   └── form.html        # 靜態輸入表單頁面 (無 CSS、無 JS)
└── templates/
    └── result.html       # 動態預測結果頁面 (無 CSS、無 JS)
```

## 安裝與啟動
```bash
pip install -r requirements.txt
python app.py
```
啟動後開啟瀏覽器造訪 http://127.0.0.1:5000/

## 規格對應說明
| 規格 | 實作方式 |
|---|---|
| 輸入表單是靜態頁面 | `GET /` 由 `send_from_directory` 直接回傳 `static/form.html`，不經過 Jinja2 樣板引擎，內容固定 |
| 結果頁面是動態頁面 | `POST /predict` 依表單數值即時計算，透過 `render_template` 動態產生 `templates/result.html` |
| 不使用 CSS / JavaScript | 兩個頁面皆為純語意化 HTML 標籤，無 `<style>`、無外部樣式表、無 `<script>`、無 on* 事件屬性 |

## 注意事項
- 原規格提到輸入 `x1, x2, x3`，但 ANN 模型需要 4 個特徵（花萼長度/寬度、花瓣長度/寬度）才能推論，
  因此表單實際上是 `x1 ~ x4` 四個輸入欄位，對應 `ann_params.yaml` 中 `feature_order` 的順序。
- 預測邏輯不重新呼叫 scikit-learn，而是直接讀取 `ann_params.yaml` 內已訓練好的權重，
  以 numpy 手動實作 `sigmoid` 前向傳遞（隱藏層與輸出層皆為 Sigmoid），與規格保持一致。
