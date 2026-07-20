# ```pinecone.models.vectors.search.SearchRecordsResponse``` 取出 ```hits``` 資料
要從 ```Pinecone Python SDK``` 的 ```SearchRecordsResponse``` 物件中取出 ```hits``` 資料，您需要透過 ```.result.hits``` 屬性路徑來存取。
以下是完整的提取方法與程式碼範例：
## 核心存取語法
```python
# 假設 response 是您的 SearchRecordsResponse 物件
hits_list = response.result.hits
```
## 完整程式碼與走訪範例
在 Pinecone 的整合式記錄（Integrated Records）架構中，hits 是一個包含多個 Hit 物件的列表（List），這些物件已依據相似度分數（Score）從高到低排序。您可以透過以下方式遍歷並提取每個欄位： [1] 
```python
# 1. 取得 hits 列表
hits = response.result.hits

# 2. 遍歷每一個搜尋結果 (Hit 物件)
for hit in hits:
    record_id = hit.id         # 記錄的唯一標記 (ID)
    score = hit.score          # 相似度分數 (Similarity Score)
    fields = hit.fields        # 包含文字或其它 metadata 的字典 (Dict)
    
    print(f"ID: {record_id}, Score: {score}")
    print(f"Fields/Data: {fields}\n")
```

## 結構說明表格

| 屬性路徑 | 資料型態 | 說明 |
|---|---|---|
| ```response.result``` | ```SearchRecordsResponseResult``` | 搜尋結果的核心主體 |
| ```response.result.hits``` | ```List[Hit]``` | 匹配成功的記錄列表（已排序） |
| ```hit.id``` | ```str``` | 該筆紀錄的 ID |
| ```hit.score``` | ```float``` | 與查詢內容的相似度分數（如餘弦相似度） |
| ```hit.fields``` | ```dict``` | 存儲的原始文字欄位或中繼資料（Metadata） |

如果您需要進一步處理 ```hit.fields``` 內的特定文字，直接使用 Python 的字典取值方式即可（例如：```hit.fields.get("text_field_name")```）。
如果您在提取過程中遇到特定欄位遺漏或返回 ```None``` 的問題，請告訴我，這通常與查詢時設定的 ```fields``` 篩選參數有關，我們可以一起排查！

[1] [https://sdk.pinecone.io](https://sdk.pinecone.io/python/how-to/integrated-records.html)
