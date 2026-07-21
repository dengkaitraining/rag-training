import yaml
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from pathlib import Path

# ---------------------------------------
# Read YAML
# ---------------------------------------
with open((Path(__file__).parent) / "ann_config.yaml", "r") as file:
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