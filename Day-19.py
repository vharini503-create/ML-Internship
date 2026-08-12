import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

print("---------- DAY 19 - CLASSIFICATION MODELS ----------")

# 1. LOAD IRIS DATASET

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:")
print(X.shape)

print("\nFeature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)

# 2. FEATURES AND TARGET

print("\nFeatures:")
print(X[:5])

print("\nTarget:")
print(y[:5])

# 3. TRAIN-TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. LOGISTIC REGRESSION

logistic_model = LogisticRegression(max_iter=200)

logistic_model.fit(X_train, y_train)

logistic_prediction = logistic_model.predict(X_test)

logistic_accuracy = accuracy_score(
    y_test,
    logistic_prediction
)

print("\nLogistic Regression Accuracy:")
print(logistic_accuracy)

# 5. DECISION TREE

decision_tree = DecisionTreeClassifier(
    random_state=42
)

decision_tree.fit(X_train, y_train)

tree_prediction = decision_tree.predict(X_test)

tree_accuracy = accuracy_score(
    y_test,
    tree_prediction
)

print("\nDecision Tree Accuracy:")
print(tree_accuracy)

# 6. KNN

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

knn_prediction = knn.predict(X_test)

knn_accuracy = accuracy_score(
    y_test,
    knn_prediction
)

print("\nKNN Accuracy:")
print(knn_accuracy)

# 7. MODEL COMPARISON

models = [
    "Logistic Regression",
    "Decision Tree",
    "KNN"
]

accuracies = [
    logistic_accuracy,
    tree_accuracy,
    knn_accuracy
]

comparison = pd.DataFrame({
    "Model": models,
    "Accuracy": accuracies
})

print("MODEL COMPARISON")

print(comparison)

# 8. BASIC VISUALIZATION

plt.figure(figsize=(8, 5))

plt.bar(models, accuracies)

plt.title("ML Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")

plt.ylim(0, 1.1)

plt.xticks(rotation=15)

plt.show()

# 9. TEST A NEW FLOWER

new_flower = [[
    5.1,
    3.5,
    1.4,
    0.2
]]

prediction = logistic_model.predict(new_flower)

print("\nPredicted Class for New Flower:")

print(iris.target_names[prediction[0]])


print("----------- DAY 19 COMPLETED ----------")
