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