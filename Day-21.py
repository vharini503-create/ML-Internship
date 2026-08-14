import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


print("---------- DAY 21 - MODEL COMPARISON ----------")


# 1. Load Iris Dataset

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:")
print(X.shape)


# 2. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. Create Models

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}


# 4. Train and Evaluate Models

results = []

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    results.append({
        "Model": name,
        "Accuracy": accuracy
    })

    print(name)
  

    print("Accuracy:", accuracy)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, prediction))


# 5. Create Comparison Table

results_df = pd.DataFrame(results)

print("MODEL COMPARISON")

print(results_df)


# 6. Find Best Model

best_model = results_df.loc[
    results_df["Accuracy"].idxmax()
]

print("\nBest Model:")
print(best_model["Model"])

print("Best Accuracy:")
print(best_model["Accuracy"])


# 7. Visualization

plt.figure(figsize=(8, 5))

plt.bar(
    results_df["Model"],
    results_df["Accuracy"]
)

plt.title("Classification Model Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy")

plt.ylim(0, 1.1)

plt.xticks(rotation=15)

plt.show()


print("---------- DAY 21 COMPLETED ----------")
