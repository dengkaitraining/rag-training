Yahoo 官方的免費金融 API 已於 2017 年正式關閉，但目前開發者主要透過開源第三方套件 yfinance 或直接呼叫隱藏的 Web API URL 來免費抓取 [Yahoo 財經](https://hk.finance.yahoo.com/quote/API/)的全球股票數據（含台股、美股、港股）。 [1, 2, 3] 
以下為您整理現行最常用的兩種實作方式：
## 方法一：使用 Python 第三方套件 yfinance（推薦）
這是目前最穩定且盛行的替代方案，它藉由模擬網頁請求來下載 Yahoo 財經的即時與歷史數據。 [1, 3] 

* 
* 安裝指令：
```sh
pip install yfinance
```

* Python 程式碼範例：
```python
import yfinance as yf
# 台股代碼需加上字尾（上市 .TW / 上櫃 .TWO）
# 例如：台積電 (2330.TW)、鴻海 (2317.TW)
ticker = "2330.TW" 
# 取得股票物件
stock = yf.Ticker(ticker)
# 1. 取得歷史股價資料 (1個月歷史，可選 1d, 5d, 1mo, 1y, max 等)
hist = stock.history(period="1mo")
print("--- 歷史股價 ---")
print(hist[['Open', 'High', 'Low', 'Close', 'Volume']])
# 2. 取得即時盤後或基本面資訊
info = stock.info
print("\n--- 股票基本資訊 ---")
print(f"公司名稱: {info.get('longName')}")
print(f"當前股價: {info.get('currentPrice')}")
print(f"本益比 (PE Ratio): {info.get('trailingPE')}")
```
* 

## 方法二：直接呼交 Yahoo 隱藏的 Chart API（適合無 Python 環境）
如果您使用的是 C#、JavaScript 或其它後端語言，可以直接對 Yahoo 內部的查詢網址發送 HTTP GET 請求。 [2, 4] 

* 
* API 查詢網址格式：
```
https://query1.finance.yahoo.com/v8/finance/chart/{股票代碼}
```
* 實際範例（台積電 2330）：
```
https://query1.finance.yahoo.com/v8/finance/chart/2330.TW
```
* 回傳格式：
回傳標準的 JSON 格式資料，包含時間戳記（Timestamp）、開盤價、最高價、最低價、收盤價及成交量等數據。 [4] 
* 

------------------------------
## ⚠️ 使用注意事項

* 
* 頻率限制：由於這些方法並非官方正式開放的商業管道，短時間內發送過於頻繁的 Request（例如每秒數十次），將會導致暫時性鎖定 IP。
* 資料延遲：免費抓取的即時數據通常會有 15 分鐘的延遲（非券商逐筆撮合的即時盤），較適合做波段分析、歷史回測或每日盤後記錄。
* 台股代碼規則：查詢台灣股市時，必須在數字代號後加上 . 與後綴（上市為 .TW，上櫃為 .TWO）。 [1, 5, 6] 
* 

如果需要串接完全即時且無延遲的台股資料，或希望進行自動化下單，建議改為申請國內券商（如[元大證券]、[永豐金證券]）免費提供的官方 券商 API。 [7, 8] 
如果您需要調整程式碼，請問您目前預計使用哪種程式語言（例如 Python、Node.js、C#）？您主要想抓取台股還是美股的資料呢？

[1] [https://www.tejwin.com](https://www.tejwin.com/insight/%E8%82%A1%E7%A5%A8api/)
[2] [https://www.reddit.com](https://www.reddit.com/r/csharp/comments/6jttuj/api_to_use_for_do_a_stock_symbol_lookup_in_c/?tl=zh-hant)
[3] [https://www.pj-worklife.com.tw](https://www.pj-worklife.com.tw/yfinance-api/)
[4] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10236119?sc=hot)
[5] [https://aronhack.com](https://aronhack.com/zh/download-stock-historical-data-with-python-and-yahoo-finance-api-zh/)
[6] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10353034)
[7] [https://www.tssco.com.tw](https://www.tssco.com.tw/585/)
[8] [https://opop.tw](https://opop.tw/program-trading-in-taiwan/)
