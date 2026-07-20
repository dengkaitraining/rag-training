from sentence_transformers import SentenceTransformer

def text_to_embedding():
    # 1. 載入 all-MiniLM-L6-v2 模型
    # 第一次執行時，程式會自動從 Hugging Face 下載模型權重（約 80MB）
    print("正在載入 all-MiniLM-L6-v2 模型，請稍候...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("模型載入完成！\n")

    # 2. 提供文字輸入欄位，讓使用者可以自由變化輸入內容
    user_input = input("請輸入想要轉換成向量的文字：")
    
    if not user_input.strip():
        print("輸入內容不能為空！")
        return

    # 3. 將文字轉換為向量 (Embedding)
    print("\n正在計算向量...")
    embedding = model.encode(user_input)

    # 4. 輸出結果
    print("\n--- 轉換結果 ---")
    print(f"輸入的文字: \"{user_input}\"")
    print(f"向量總維度 (Dimensions): {len(embedding)}")
    
    # 取出前 10 個元素並格式化輸出
    first_10_elements = embedding[:10]
    print("向量的前 10 個元素為:")
    print("[ " + ", ".join([f"{val:.16f}" for val in first_10_elements]) + ", ... ]")

if __name__ == "__main__":
    text_to_embedding()