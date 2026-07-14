import os
from dotenv import load_dotenv

# 載入同目錄下的 .env 檔案
load_dotenv()

# 讀取 privateKey 環境變數
privateKey = os.getenv("privateKey", "")
if not privateKey:
    raise ValueError("找不到 privateKey，請先設定環境變數")
else:
    print(f"privateKey 已成功讀取: {privateKey}")

# 讀取 publickey 環境變數
publickey = os.getenv("publickey", "")
if not publickey:
    raise ValueError("找不到 publickey，請先設定環境變數")
else:
    print(f"publickey 已成功讀取: {publickey}")

# 讀取 headers 環境變數
headers = os.getenv("headers", "")
if not headers:
    raise ValueError("找不到 headers，請先設定環境變數")
else:
    print(f"headers 已成功讀取: {headers}")

# 讀取 payload 環境變數
payload = os.getenv("payload", "")
if not payload:
    raise ValueError("找不到 payload，請先設定環境變數")
else:
    print(f"payload 已成功讀取: {payload}")

# 讀取 pyjwt 環境變數
pyjwt = os.getenv("pyjwt", "")
if not pyjwt:
    raise ValueError("找不到 pyjwt，請先設定環境變數")
else:
    print(f"pyjwt 已成功讀取: {pyjwt}")