import re

def extract_tech_keywords(user_prompt: str) -> list:
    """
    檢查 user_prompt 中是否包含 AI, IoT, Blockchain 等關鍵字。
    - 關鍵字如果是英文單字的一部分（如 paint 裡的 ai），視為未比對到。
    - 關鍵字如果出現在非英文詞後（如 '中文AI'、'標點!AI'、'空格 AI'），視為比對到。
    """
    keywords = ["AI", "IoT", "Blockchain"]
    
    # 用 | 將關鍵字結合
    joined_keywords = '|'.join(keywords)
    
    # (?<![a-zA-Z]) 代表左邊不能是英文字母
    # (?![a-zA-Z])  代表右邊不能是英文字母
    pattern = rf'(?<![a-zA-Z])({joined_keywords})(?![a-zA-Z])'
    
    # 進行不區分大小寫的比對
    matches = re.findall(pattern, user_prompt, re.IGNORECASE)
    
    return matches

if __name__ == "__main__":
    test_cases = [
        # 1. 出現於非英文詞（中文）後面 -> 應該比對到
        "這台IoT設備很棒", 
        "我對AI很有興趣",
    
        # 2. 出現於空格或標點符號後 -> 應該比對到
        "I like AI.",
        "Blockchain, IoT, and AI are trending.",
    
        # 3. 屬於英文單字的一部分 -> 應該忽略（未比對到）
        "Let's paint a picture.",        # paint 含有 ai -> 忽略
        "Biotech is expanding.",         # biotech 含有 iot -> 忽略
        "The blockchaining process...",  # blockchaining 含有 blockchain -> 忽略
    
        # 4. 混合極端情況
        "這是一個畫畫paint與AI的結合",    # 應只抓到 'AI'，忽略 'paint' 中的 ai
    ]

    for text in test_cases:
        result = extract_tech_keywords(text)
        #print(f"輸入: {text:<28} -> 偵測結果: {result}")
        print(f"---\n輸入文字: {text:<28}  \n偵測結果: {result}")
    print("---")