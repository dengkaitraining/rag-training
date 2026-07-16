import re

def extract_tech_keywords(user_prompt):
    """
    比對 User_Prompt 是否包含 AI, IoT, Blockchain 等關鍵字。
    - 若為英文 vocabulary 的一部分（前後緊接英文字母）則視為未比對到。
    - 若出現在非英文詞（如中文、標點符號、空白）前後，則當作比對到。
    """
    
    # 定義正規表達式
    # (?<![a-zA-Z]) : 確保前面不是英文字母
    # (AI|IoT|Blockchain) : 比對的關鍵字群組
    # (?![a-zA-Z])  : 確保後面不是英文字母
    pattern = r'(?<![a-zA-Z])(AI|IoT|Blockchain)(?![a-zA-Z])'
    
    # 使用 re.findall 找出所有符合的字串
    # 加入 re.IGNORECASE 讓比對不區分大小寫
    matches = re.findall(pattern, user_prompt, flags=re.IGNORECASE)
    
    return matches

# ==========================================
# 測試範例 (Test Cases)
# ==========================================
if __name__ == "__main__":
    test_cases = [
        "這是AI的應用。",                 # [預期有] 緊接在中文後面
        "關於IoT的發展，還有Blockchain技術", # [預期有] 中文與英文混合
        "The project ends in fAIlure.",   # [預期無] AI 是 failure 的一部分
        "Don't be an idiot.",             # [預期無] iot 是 idiot 的一部分
        "Let's build a new blockchain!",  # [預期有] 前面是空白，後面是標點符號
        "SmartContractBlockchainTest"     # [預期無] 夾在英文單字中間
    ]

    for prompt in test_cases:
        result = extract_tech_keywords(prompt)
        print(f"輸入: {prompt}")
        print(f"結果: {result}")
        print("-" * 40)
