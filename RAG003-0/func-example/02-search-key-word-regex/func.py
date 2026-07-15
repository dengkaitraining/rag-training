import re
import os
from pathlib import Path

def search_knowledge_by_keyword(keyword: str, file_path: str = Path(__file__).parent / "knowledge.txt") -> list:
    """
    從指定的知識庫檔案中，搜尋與給定關鍵字相符的所有描述。
    
    :param keyword: 欲搜尋的關鍵字（例如 'AI' 或 'IoT'）
    :param file_path: 知識庫檔案路徑，預設為 'knowledge.txt'
    :return: 包含所有對應描述內容的 list。若無比對到，則回傳空 list []。
    """
    # 檢查檔案是否存在，若不存在則回傳空 list
    if not os.path.exists(file_path):
        print(f"錯誤：找不到檔案 {file_path}")
        return []
        
    results = []
    
    # 正規表示式解析規則：
    # ^\s*([^,\s]+)  : 匹配行首可能存在的空白，並抓取不包含逗號與空白的「關鍵字」
    # \s*,\s*        : 匹配關鍵字與雙引號之間的逗號，並忽略前後多餘空白
    # "(.*)"\s*$     : 匹配被雙引號 " " 包裹起來的「描述內容」，並抓取引號內的所有字元
    pattern = re.compile(r'^\s*([^,\s]+)\s*,\s*"(.*)"\s*$')
    
    # 讀取檔案進行比對
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行尾換行符號
            line = line.strip()
            if not line:
                continue
                
            # 使用 re 比對該行結構
            match = pattern.match(line)
            if match:
                file_keyword, description = match.groups()
                
                # 進行不區分大小寫的關鍵字比對 (若需嚴格區分大小寫，可改為: if file_keyword == keyword)
                if file_keyword.strip().lower() == keyword.strip().lower():
                    results.append(description)
                    
    return results

if __name__ == "__main__":
    # 1. 搜尋關鍵字 "AI"
    ai_results = search_knowledge_by_keyword("AI")
    print("【AI 的搜尋結果】:")
    for idx, desc in enumerate(ai_results, 1):
        print(f"{idx}. {desc}")

    print("-" * 50)

    # 2. 搜尋關鍵字 "IoT" (測試小寫輸入是否能對應)
    iot_results = search_knowledge_by_keyword("iot")
    print("【IoT 的搜尋結果】:")
    for idx, desc in enumerate(iot_results, 1):
        print(f"{idx}. {desc}")

    print("-" * 50)

    # 3. 搜尋不存在的關鍵字 "Blockchain"
    blockchain_results = search_knowledge_by_keyword("Blockchain")
    print(f"【Blockchain 的搜尋結果】: {blockchain_results}")