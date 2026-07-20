from sentence_transformers import SentenceTransformer, util

def compare_sentences_loop():
    # 1. 載入 all-MiniLM-L6-v2 模型
    print("正在載入 all-MiniLM-L6-v2 模型，請稍候...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("模型載入完成！開始進行語意相似度比較。")
    print("（提示：在任何輸入欄位輸入 'q' 即可退出程式）\n")

    # 2. 進入互動式迴圈
    while True:
        print("-" * 50)
        # 輸入第一段文字
        text1 = input("請輸入第一段文字: ").strip()
        if text1.lower() == 'q':
            print("程式已結束。")
            break
        if not text1:
            print("❌ 輸入不能為空，請重新輸入。")
            continue

        # 輸入第二段文字
        text2 = input("請輸入第二段文字: ").strip()
        if text2.lower() == 'q':
            print("程式已結束。")
            break
        if not text2:
            print("❌ 輸入不能為空，請重新輸入。")
            continue

        # 3. 將兩段文字分別轉成向量
        embedding1 = model.encode(text1, convert_to_tensor=True)
        embedding2 = model.encode(text2, convert_to_tensor=True)

        # 4. 計算 Cosine Similarity (餘弦相似度)
        # util.cos_sim 會回傳一個 PyTorch Tensor 二維矩陣，我們取出數值即可
        similarity = util.cos_sim(embedding1, embedding2).item()

        # 5. 輸出結果
        print(f"\n👉 相似度分析結果:")
        print(f"   [文字 A]: {text1}")
        print(f"   [文字 B]: {text2}")
        print(f"   ➡️ 餘弦相似度 (Cosine Similarity): {similarity:.8f}")
        
        # 給予直觀的語意判斷提示
        if similarity > 0.8:
            print("   💡 評語: 這兩句話語意極度相似！")
        elif similarity > 0.5:
            print("   💡 評語: 這兩句話有高度相關性。")
        elif similarity > 0.2:
            print("   💡 評語: 這兩句話有些微關聯。")
        else:
            print("   💡 評語: 這兩句話幾乎沒有關聯。")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    # 請確保檔案名稱「不是」sentence_transformers.py 喔！
    compare_sentences_loop()