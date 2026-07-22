# **vector similarity**
![](images/vector-similarity.png)

 - **Prompt 描述**
   ```txt
   請將「圖片 vector-similarity.png」轉換為 mermaid 格式的向量座標構圖，並以 subgraph 方式保留「圖片 vector-similarity.png」layout 的樣式。
   ```
 - **Mermaid 格式**
```mermaid
flowchart TD
    %% 上半部分：模型流程
    subgraph Upper ["嵌入式模型流程 (Embedding Process)"]
        direction LR
        Input["a piece of info."] -- "輸入" --> Model["嵌入式模型"]
        Model -- "輸出" --> Output["a vector with high dimension"]
    end

    %% 下半部分：向量空間與公式
    subgraph Lower ["向量空間與相似度計算 (Vector Space & Similarity)"]
        direction LR
        
        %% 模擬座標軸與向量
        subgraph VectorGraph ["向量座標構圖"]
            direction BT
            Origin["原點 (0,0)"]
            AxisY["Y 軸"]
            AxisX["X 軸"]
            
            Origin -->|Vector A| VectorA["向量 A"]
            Origin -->|Vector B| VectorB["向量 B"]
            Origin -.->|夾角 θ| Angle["θ"]
        end

        %% 數學公式節點
        subgraph Formula ["餘弦相似度公式"]
            Math["cos(θ) = (A · B) / (||A|| · ||B||)"]
        end
    end

    %% 樣式設定
    classDef modelStyle fill:#fff,stroke:#000,stroke-width:2px,font-weight:bold;
    classDef infoStyle fill:#fff,stroke:none,color:#b22222,font-weight:bold;
    classDef vectorStyle fill:#fff,stroke:none,color:#1e90ff,font-weight:bold;
    classDef mathStyle fill:#f9f9f9,stroke:#333,stroke-width:1px,font-size:18px;

    class Model modelStyle;
    class Input infoStyle;
    class Output vectorStyle;
    class Math mathStyle;
    
    %% 調整子圖外觀
    style Upper fill:#fdfdfd,stroke:#ddd,stroke-width:1px
    style Lower fill:#fdfdfd,stroke:#ddd,stroke-width:1px
    style VectorGraph fill:#fff,stroke:#eee
    style Formula fill:#fff,stroke:#eee
```

# **vector db**
![](images/vector-db.png)

# **embedding model**
![](images/embedding-model.png)