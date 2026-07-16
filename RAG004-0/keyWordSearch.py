import re
import os

def find_knowledge_by_keyword(keyword, file_path="knowledge.txt"):
    """
    從指定的知識庫檔案中，找出對應關鍵字的所有描述。
    
    :param keyword: 要搜尋的關鍵字 (例如: "AI", "IoT")
    :param file_path: 檔案路徑，預設為 "knowledge.txt"
    :return: 包含所有對應描述的 list，若未比對到或檔案不存在則回傳空 list []
    """
    results = []
    
    # 1. 安全檢查：確認檔案是否存在
    if not os.path.exists(file_path):
        print(f"提示：找不到檔案 {file_path}")
        return results
        
    # 2. 定義解析每行格式的正規表達式
    # ^\s*([^,]+?) : 從開頭匹配「非逗號」的字元作為關鍵字，並自動忽略前面的空白
    # \s*,\s* : 匹配關鍵字與雙引號之間的逗號，並忽略其前後的空白
    # "(.*?)"      : 匹配被雙引號 " 包含起來的描述內容（Group 2）
    # \s*$         : 確保結尾，並忽略後方的空白
    line_pattern = r'^\s*([^,]+?)\s*,\s*"(.*?)"\s*$'
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # 跳過空行
                
                # 使用 re.match 進行整行解析
                match = re.match(line_pattern, line)
                
                if match:
                    parsed_keyword = match.group(1)   # 萃取出的關鍵字
                    description = match.group(2)      # 萃取出的描述內容
                    
                    # 進行比對（此處採用「忽略大小寫」的比對，若要嚴格比對可改為 parsed_keyword == keyword）
                    if parsed_keyword.lower() == keyword.lower():
                        results.append(description)
                else:
                    # 格式不符時的提示（可選）
                    print(f"警告：第 {line_number} 行格式不符，已跳過：{line}")
                    
    except IOError as e:
        print(f"讀取檔案時發生錯誤: {e}")
        
    return results

# ==========================================
# 測試與示範 (Test Cases)
# ==========================================
if __name__ == "__main__":
    # 模擬建立測試用的 knowledge.txt 檔案
    sample_content = """AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
"""
    
    with open("knowledge.txt", "w", encoding="utf-8") as f:
        f.write(sample_content)
        
    print("--- 測試檔案 knowledge.txt 建立成功 ---\n")
    
    # 測試 1：搜尋 "AI"
    ai_results = find_knowledge_by_keyword("AI")
    print(ai_results)
    context="。".join(ai_results)
    print(context)
    print("【搜尋 AI 的結果】:")
    for idx, desc in enumerate(ai_results, 1):
        print(f"{idx}. {desc}")
    print("-" * 50)
    
    # 測試 2：搜尋 "IoT" (測試小寫輸入也能對應)
    iot_results = find_knowledge_by_keyword("iot")
    print("【搜尋 iot 的結果】:")
    for idx, desc in enumerate(iot_results, 1):
        print(f"{idx}. {desc}")
    print("-" * 50)
    
    # 測試 3：搜尋不存在的關鍵字 "Blockchain"
    blockchain_results = find_knowledge_by_keyword("Blockchain")
    print(f"【搜尋 Blockchain 的結果】: {blockchain_results}")
