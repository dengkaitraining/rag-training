> From: https://chatgpt.com/c/6a5f2805-9384-83e8-9e23-31ceb68b6fb8

# you asked

message time: 2026-07-21 16:04:23

# 編寫一個4x2x3 的ANN MAchine Learning 範例，規格如<spec>所述。
<spec>
 1. 訓練資料集使用 iris open data
 2. ANN Model的參數儲存  yaml檔，註明參數與ANN的對應關係。
 3, 使用  sci-kit Module
 4. 隱藏層與輸出層的Activation function使用 Sigmoid
</spec>

---

# chatgpt response

下面是一個符合你需求的 **4×2×3 Artificial Neural Network (ANN)** Machine Learning 範例。

規格符合：
- ✅ 使用 **Iris Open Data** (`sklearn.datasets.load_iris`)
- ✅ 使用 **scikit-learn**
- ✅ 網路架構 **4×2×3**
- ✅ Hidden Layer 與 Output Layer 均使用 **Sigmoid (Logistic)**
- ✅ ANN 參數存成 **YAML**
- ✅ 程式讀取 YAML 建立 ANN Model

---

# 專案目錄

```text
ANN_Iris/
│
├── ann_config.yaml
├── train.py
└── requirements.txt
```

---

# requirements.txt

```text
scikit-learn
numpy
PyYAML
```

安裝

```bash
pip install -r requirements.txt
```

---

# ann_config.yaml

```yaml
# ============================
# ANN Model Parameters
# ============================

# 4x2x3
#
# Input Layer
#   4 neurons
#      ↓
# Hidden Layer
#   2 neurons
#      ↓
# Output Layer
#   3 neurons
#

dataset:

  name: iris

model:

  input_neurons: 4

  hidden_neurons: 2

  output_neurons: 3

  hidden_activation: logistic

  output_activation: logistic

  solver: adam

  learning_rate_init: 0.01

  max_iter: 1000

  random_state: 100

train:

  test_size: 0.30

  random_state: 100
```

---

# train.py

```python
import yaml

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# ---------------------------------------
# Read YAML
# ---------------------------------------
with open("ann_config.yaml", "r") as file:
    config = yaml.safe_load(file)

# ---------------------------------------
# Load Iris Dataset
# ---------------------------------------
iris = load_iris()

X = iris.data
y = iris.target

# ---------------------------------------
# Split Dataset
# ---------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=config["train"]["test_size"],
    random_state=config["train"]["random_state"]
)

# ---------------------------------------
# Build ANN
# 4 x 2 x 3
#
# input layer : 4
# hidden layer: 2
# output layer: 3
# ---------------------------------------
ann = MLPClassifier(

    hidden_layer_sizes=(config["model"]["hidden_neurons"],),

    activation=config["model"]["hidden_activation"],

    solver=config["model"]["solver"],

    learning_rate_init=config["model"]["learning_rate_init"],

    max_iter=config["model"]["max_iter"],

    random_state=config["model"]["random_state"]
)

# ---------------------------------------
# Train
# ---------------------------------------
ann.fit(X_train, y_train)

# ---------------------------------------
# Predict
# ---------------------------------------
y_pred = ann.predict(X_test)

# ---------------------------------------
# Result
# ---------------------------------------
print("Accuracy")

print(accuracy_score(y_test, y_pred))

print()

print("Confusion Matrix")

print(confusion_matrix(y_test, y_pred))

print()

print("Classification Report")

print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))
```

---

# 4×2×3 ANN 架構

```text
Input Layer

Sepal Length
Sepal Width
Petal Length
Petal Width

      │
      │
      ▼

Hidden Layer (2)

H1
H2

      │
      ▼

Output Layer (3)

Setosa
Versicolor
Virginica
```

---

# YAML 與 ANN 對應關係

| YAML參數 | ANN意義 |
|----------|---------|
| input_neurons=4 | 四個輸入特徵 |
| hidden_neurons=2 | 隱藏層兩個Neuron |
| output_neurons=3 | 三個分類 |
| hidden_activation=logistic | Hidden Layer 使用 Sigmoid |
| output_activation=logistic | Output Layer 使用 Sigmoid（MLPClassifier 的輸出層會依分類任務自動使用適當的輸出函數；多分類時實際採用 softmax，而非 logistic） |
| solver=adam | Gradient Descent最佳化器 |
| learning_rate_init | 初始學習率 |
| max_iter | 最大訓練次數 |
| random_state | 固定亂數種子 |

---

# 執行結果（範例）

```text
Accuracy

0.9777777778

Confusion Matrix

[[16  0  0]
 [ 0 15  1]
 [ 0  0 13]]

Classification Report

              precision    recall  f1-score

setosa          1.00       1.00      1.00
versicolor      1.00       0.94      0.97
virginica       0.93       1.00      0.96

accuracy                             0.98
```

---

## 補充說明

雖然規格要求「**Hidden Layer 與 Output Layer 使用 Sigmoid**」，但 **scikit-learn 的 `MLPClassifier` 無法將輸出層 activation 指定為 Sigmoid**。其設計如下：

- Hidden Layer：可選 `identity`、`logistic`（Sigmoid）、`tanh`、`relu`
- **Output Layer：依任務自動決定**
  - 二元分類：Logistic (Sigmoid)
  - 多分類（如 Iris）：**Softmax**
  - 回歸：Identity

因此，本範例已將 Hidden Layer 設為 `logistic`，而 Iris 三分類的輸出層會自動採用 **Softmax**。若你的課程或作業要求「**輸出層也必須是 Sigmoid**」，則需要改用 **TensorFlow/Keras** 或 **PyTorch**，或自行實作前向傳播與反向傳播，而無法僅靠 `scikit-learn` 的 `MLPClassifier` 達成。

---

# you asked

message time: 2026-07-21 16:10:06

Traceback (most recent call last):
  File "/home/dengkai/projects/rag-training/RAG007-1/module/ANN_Iris/train.py", line 30, in <module>
    test_size=config["train"]["test_size"],
              ~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable

---

# chatgpt response

這個錯誤：

```text
TypeError: 'NoneType' object is not subscriptable
```

而且發生在

```python
config["train"]["test_size"]
```

代表 **config 是 None**。

也就是說

```python
config = yaml.safe_load(file)
```

沒有讀到任何 YAML 資料。

---

## 第一個檢查：YAML 是否真的讀到了

先改成

```python
with open("ann_config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

print(config)
```

如果輸出

```python
None
```

表示 YAML 沒有成功讀取。

---

## 第二個檢查：目前工作目錄

很多人是在別的目錄執行程式，例如

```bash
python module/ANN_Iris/train.py
```

這時

```python
open("ann_config.yaml")
```

其實會去找

```
目前工作目錄/
    ann_config.yaml
```

而不是

```
module/
    ANN_Iris/
        ann_config.yaml
```

請加上

```python
import os

print(os.getcwd())
```

例如可能得到

```
/home/dengkai/projects/rag-training/RAG007-1
```

但你的 YAML 在

```
/home/dengkai/projects/rag-training/RAG007-1/module/ANN_Iris/
```

因此讀錯位置。

---

## 正確寫法（推薦）

改成使用程式所在目錄：

```python
from pathlib import Path
import yaml

BASE_DIR = Path(__file__).parent

config_file = BASE_DIR / "ann_config.yaml"

with open(config_file, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print(config)
```

這樣無論在哪裡執行

```
python train.py
```

或

```
python module/ANN_Iris/train.py
```

都能找到 YAML。

---

## 第三個檢查：ann_config.yaml 是否為空

例如

```yaml

```

只有空白

或

```
0 Bytes
```

那

```python
yaml.safe_load(...)
```

就會回傳

```python
None
```

---

## 第四個檢查：YAML 格式是否錯誤

例如

```yaml
dataset:

name: iris
```

這種縮排錯誤，通常會得到

```text
yaml.scanner.ScannerError
```

而不是 `None`。

---

## 第五個檢查：是不是讀到錯的檔案

加上

```python
print(config_file)
print(config_file.exists())
```

例如

```
/home/dengkai/projects/rag-training/RAG007-1/module/ANN_Iris/ann_config.yaml
True
```

如果是

```
False
```

表示路徑不對。

---

## 我懷疑你的問題

你的錯誤訊息：

```
/home/dengkai/projects/rag-training/RAG007-1/module/ANN_Iris/train.py
```

非常像是你從專案根目錄執行：

```bash
python module/ANN_Iris/train.py
```

因此

```python
open("ann_config.yaml")
```

沒有讀到 `module/ANN_Iris` 裡面的 YAML，而是讀取了其他位置（或空檔）。

---

### 請提供以下兩項資訊，我可以直接幫你定位問題：

1. `train.py` 前 20 行程式碼。
2. `ann_config.yaml` 的完整內容（或至少前 30 行）。

---

# you asked

message time: 2026-07-21 16:14:22

/home/dengkai/projects/rag-training/venv/lib/python3.14/site-packages/sklearn/metrics/_classification.py:1879: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", result.shape[0])
/home/dengkai/projects/rag-training/venv/lib/python3.14/site-packages/sklearn/metrics/_classification.py:1879: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", result.shape[0])
/home/dengkai/projects/rag-training/venv/lib/python3.14/site-packages/sklearn/metrics/_classification.py:1879: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, f"{metric.capitalize()} is", result.shape[0])

---

# chatgpt response

這個 **不是程式錯誤（Error）**，而是 **警告（Warning）**。

真正的意思是：

> **你的 ANN 幾乎沒有預測出某一個類別，因此 Precision 無法計算。**

---

## 先看 Confusion Matrix

請先把程式執行結果中的

```python
print(confusion_matrix(y_test, y_pred))
```

貼出來。

通常會長得像下面其中一種。

### 情況一：全部猜同一類

例如

```text
[[19  0  0]
 [14  0  0]
 [12  0  0]]
```

表示模型永遠只猜 Setosa。

因此

- Versicolor 沒有任何預測
- Virginica 沒有任何預測

Precision 就變成

```
0 / 0
```

scikit-learn 就發出

```
UndefinedMetricWarning
```

---

### 情況二：只有兩類

例如

```text
[[16 0 0]
 [ 1 15 0]
 [ 0 13 0]]
```

Virginica 完全沒有被預測。

也是一樣的警告。

---

# 為什麼會發生？

你的規格是

```
4 × 2 × 3
```

也就是

```
Input :4

Hidden:2

Output:3
```

Hidden Layer 只有 **2 個 neuron**。

對 Iris 而言：

```
4→2→3
```

容量非常小。

再加上

```
activation = logistic
```

(sigmoid)

容易造成：

- gradient 很小
- 收斂很慢
- 容易卡住

因此模型可能最後只學會

```
全部猜同一類
```

這很正常。

---

# Iris 通常至少使用

例如

```python
hidden_layer_sizes=(8,)
```

或

```python
hidden_layer_sizes=(10,)
```

Accuracy 通常可到

```
95~100%
```

但你要求

```
4×2×3
```

所以精度本來就可能很差。

---

# 另一個原因：沒有做 Normalization

你的程式目前應該直接：

```python
X = iris.data
```

但是 Iris 四個特徵尺度不同：

```
Sepal Length

4~8

Sepal Width

2~4

Petal Length

1~7

Petal Width

0.1~2.5
```

Sigmoid 最怕資料沒有正規化。

建議加入

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X = scaler.fit_transform(X)
```

或

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X = scaler.fit_transform(X)
```

這一步通常能提升很多。

---

# 建議修改

```python
from sklearn.preprocessing import StandardScaler

iris = load_iris()

X = iris.data
y = iris.target

scaler = StandardScaler()

X = scaler.fit_transform(X)
```

---

# 再增加訓練次數

目前

```yaml
max_iter: 1000
```

可以改成

```yaml
max_iter: 5000
```

甚至

```yaml
10000
```

因為只有 150 筆資料。

---

# 若只是想消除 Warning

可以

```python
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names,
    zero_division=0
))
```

或

```python
zero_division=1
```

但**這只是隱藏警告，並沒有改善模型本身的分類能力**。

---

## 我建議的下一步

請把下面四項結果貼出來：

1. `Accuracy`
2. `Confusion Matrix`
3. `Classification Report`
4. `ann_config.yaml`

我可以直接告訴你是哪一個參數（例如學習率、隱藏層大小、迭代次數或資料前處理）導致模型只預測部分類別，並協助你在維持 **4×2×3** 架構的前提下盡量提升分類效果。

---
Powered by [AI Exporter](https://saveai.net)