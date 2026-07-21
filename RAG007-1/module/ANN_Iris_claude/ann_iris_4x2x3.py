# -*- coding: utf-8 -*-
"""
ANN (4-2-3) 範例：使用 scikit-learn 訓練 Iris 資料集
====================================================

網路架構
--------
    輸入層 (Input Layer)   : 4 個神經元 -> 對應 iris 的 4 個特徵
    隱藏層 (Hidden Layer)  : 2 個神經元 -> activation = Sigmoid (logistic)
    輸出層 (Output Layer)  : 3 個神經元 -> 對應 3 個花種類別

規格對應
--------
    1. 訓練資料集使用 iris open data      -> sklearn.datasets.load_iris()
    2. ANN 參數儲存 yaml 檔                -> ann_params.yaml (含參數與網路對應說明)
    3. 使用 scikit-learn 模組              -> sklearn.neural_network.MLPClassifier
    4. 隱藏層與輸出層 Activation 皆為 Sigmoid
       - 隱藏層: MLPClassifier(activation='logistic') 原生支援 sigmoid
       - 輸出層: scikit-learn 的 MLPClassifier 對多類別分類問題，其輸出層
         內部固定使用 softmax（搭配 cross-entropy loss），並未開放讓使用者
         更改輸出層的 activation function。
         為了符合「輸出層也使用 Sigmoid」的規格，本範例在訓練完成後，
         額外取出 sklearn 訓練好的權重 (coefs_) 與偏差值 (intercepts_)，
         自行以 numpy 實作一個「手動前向傳遞 (manual forward pass)」，
         讓輸出層改用 Sigmoid 計算（而非 sklearn 內部的 softmax），
         並比較兩者的預測結果。
         這部分會在下面程式碼與註解中明確標示。
"""

import numpy as np
import yaml
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from pathlib import Path

RANDOM_STATE = 42

# ----------------------------------------------------------------------
# 1. 讀取 Iris 資料集 (iris open data)
# ----------------------------------------------------------------------
iris = load_iris()
X = iris.data          # shape: (150, 4) -> 4 個特徵 = 輸入層 4 個神經元
y = iris.target        # shape: (150,)   -> 0/1/2 三個類別 = 輸出層 3 個神經元
feature_names = iris.feature_names
target_names = iris.target_names.tolist()

# ----------------------------------------------------------------------
# 2. 切分訓練/測試集，並做標準化 (ANN 對輸入尺度敏感，標準化有助收斂)
# ----------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ----------------------------------------------------------------------
# 3. 建立 4-2-3 ANN 模型 (使用 scikit-learn MLPClassifier)
#    hidden_layer_sizes=(2,) -> 只有一層隱藏層，2 個神經元
#    activation='logistic'   -> 隱藏層使用 Sigmoid
# ----------------------------------------------------------------------
model = MLPClassifier(
    hidden_layer_sizes=(2,),
    activation="logistic",   # Sigmoid，對應規格第4點（隱藏層）
    solver="adam",
    max_iter=5000,
    random_state=RANDOM_STATE,
)

model.fit(X_train_scaled, y_train)

# ----------------------------------------------------------------------
# 4. 模型評估 (sklearn 原生 predict，輸出層內部為 softmax)
# ----------------------------------------------------------------------
y_pred_sklearn = model.predict(X_test_scaled)
acc_sklearn = accuracy_score(y_test, y_pred_sklearn)
print(f"[sklearn 原生 MLPClassifier 準確率 (輸出層為 softmax)] : {acc_sklearn:.4f}")

# ----------------------------------------------------------------------
# 5. 取出訓練好的權重與偏差值
#    coefs_[0]      : 輸入層 -> 隱藏層 的權重矩陣, shape (4, 2)
#    intercepts_[0] : 隱藏層的偏差值 (bias),      shape (2,)
#    coefs_[1]      : 隱藏層 -> 輸出層 的權重矩陣, shape (2, 3)
#    intercepts_[1] : 輸出層的偏差值 (bias),      shape (3,)
# ----------------------------------------------------------------------
W1 = model.coefs_[0]        # (4, 2)
b1 = model.intercepts_[0]   # (2,)
W2 = model.coefs_[1]        # (2, 3)
b2 = model.intercepts_[1]   # (3,)


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def manual_forward_sigmoid_output(X_scaled):
    """
    手動前向傳遞，隱藏層與輸出層皆使用 Sigmoid，
    以完全符合規格「隱藏層與輸出層 activation 皆為 Sigmoid」。

    注意：sklearn 的 MLPClassifier 在多類別分類時，輸出層內部固定使用
    softmax，本函式僅用於示範「若輸出層改用 Sigmoid」時的計算方式，
    並非取代 sklearn 的原生 predict。
    """
    hidden_input = X_scaled @ W1 + b1          # (n, 2)
    hidden_output = sigmoid(hidden_input)      # 隱藏層 activation = Sigmoid

    output_input = hidden_output @ W2 + b2     # (n, 3)
    output_output = sigmoid(output_input)      # 輸出層 activation = Sigmoid (依規格)

    # 每個輸出神經元各自獨立經過 Sigmoid（非 softmax 的機率分佈），
    # 取值最大的神經元視為預測類別
    predicted_class = np.argmax(output_output, axis=1)
    return hidden_output, output_output, predicted_class


hidden_out_test, output_out_test, y_pred_manual = manual_forward_sigmoid_output(X_test_scaled)
acc_manual = accuracy_score(y_test, y_pred_manual)
print(f"[手動 Sigmoid 輸出層前向傳遞 準確率]                 : {acc_manual:.4f}")

# ----------------------------------------------------------------------
# 6. 將 ANN 參數儲存為 YAML，並清楚註明參數與網路架構的對應關係
# ----------------------------------------------------------------------
ann_params = {
    "model_description": "4x2x3 ANN (Iris dataset) - trained with scikit-learn MLPClassifier",
    "architecture": {
        "input_layer": {
            "neurons": 4,
            "description": "對應 iris 4 個特徵 (input features)",
            "feature_order": feature_names,
        },
        "hidden_layer": {
            "neurons": 2,
            "activation": "sigmoid",
            "description": "隱藏層，2 個神經元，activation function 為 Sigmoid",
        },
        "output_layer": {
            "neurons": 3,
            "activation": "sigmoid",
            "description": (
                "輸出層，3 個神經元，對應 3 個花種類別。"
                "依規格使用 Sigmoid；sklearn 訓練時內部使用 softmax，"
                "此處另以手動前向傳遞方式套用 Sigmoid（見 forward_pass_note）。"
            ),
            "class_order": target_names,
        },
    },
    "parameters": {
        "W1_input_to_hidden": {
            "shape": list(W1.shape),
            "meaning": "輸入層(4) -> 隱藏層(2) 的權重矩陣, W1[i][j] = 第 i 個輸入特徵 到 第 j 個隱藏神經元的權重",
            "value": W1.tolist(),
        },
        "b1_hidden_bias": {
            "shape": list(b1.shape),
            "meaning": "隱藏層 2 個神經元各自的偏差值 (bias)",
            "value": b1.tolist(),
        },
        "W2_hidden_to_output": {
            "shape": list(W2.shape),
            "meaning": "隱藏層(2) -> 輸出層(3) 的權重矩陣, W2[j][k] = 第 j 個隱藏神經元 到 第 k 個輸出神經元(類別)的權重",
            "value": W2.tolist(),
        },
        "b2_output_bias": {
            "shape": list(b2.shape),
            "meaning": "輸出層 3 個神經元(類別)各自的偏差值 (bias)",
            "value": b2.tolist(),
        },
    },
    "preprocessing": {
        "scaler": "StandardScaler",
        "mean": scaler.mean_.tolist(),
        "scale": scaler.scale_.tolist(),
        "note": "推論前，輸入特徵須先以 (x - mean) / scale 標準化，才能套用 W1/b1",
    },
    "forward_pass_note": (
        "hidden = sigmoid(X_scaled @ W1 + b1); "
        "output = sigmoid(hidden @ W2 + b2); "
        "predicted_class = argmax(output)"
    ),
    "training_config": {
        "solver": "adam",
        "max_iter": 5000,
        "random_state": RANDOM_STATE,
        "sklearn_hidden_activation": "logistic (sigmoid)",
        "sklearn_output_activation_internal": "softmax (sklearn 內部固定行為，非本範例設定)",
    },
    "evaluation": {
        "accuracy_sklearn_native_predict": float(acc_sklearn),
        "accuracy_manual_sigmoid_output": float(acc_manual),
    },
}

with open((Path(__file__).parent) / "ann_params.yaml", "w", encoding="utf-8") as f:
    yaml.dump(ann_params, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("\n已將 ANN 參數與架構對應關係儲存至 ann_params.yaml")
