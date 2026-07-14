import jwt, os, time, json
from jwt.algorithms import RSAAlgorithm
from dotenv import load_dotenv

# 載入同目錄下的 .env 檔案
load_dotenv()
"""
privateKey = json.loads(os.getenv("privateKey", ""))
headers = json.loads(os.getenv("headers", ""))
payload = json.loads(os.getenv("payload", ""))
"""
privateKey = (os.getenv("privateKey", ""))
# 讀取 privateKey 環境變數
privateKey = os.getenv("privateKey", "")
if not privateKey:
    raise ValueError("找不到 privateKey，請先設定環境變數")
else:
    print(f"privateKey 已成功讀取: {privateKey}")

headers = (os.getenv("headers", ""))
# 讀取 headers 環境變數
headers = os.getenv("headers", "")
if not headers:
    raise ValueError("找不到 headers，請先設定環境變數")
else:
    print(f"headers 已成功讀取: {headers}")

payload = (os.getenv("payload", ""))
# 讀取 payload 環境變數
payload = os.getenv("payload", "")
if not payload:
    raise ValueError("找不到 payload，請先設定環境變數")
else:
    print(f"payload 已成功讀取: {payload}")

try:
    key = RSAAlgorithm.from_jwk(privateKey)
    print(key)

    try:
        JWT = jwt.encode(payload, key, algorithm="RS256", headers=headers, json_encoder=None)
        print(JWT)
    except:
        raise ValueError("JWT 生成失敗，請確認 payload 與 headers 是否為有效的 JSON 格式")

except:
    raise ValueError("privateKey 格式錯誤，請確認是否為有效的 JWK 格式")