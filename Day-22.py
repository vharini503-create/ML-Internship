import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


print("DAY 22 - KNN HYPERPARAMETER TUNING")


# 1. Load Dataset

iris = load_iris()

X = iris.data
y = iris.target


# 2. Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. Test Different K Values

k_values = range(1, 11)

accuracies = []

for k in k_values:

    model = KNeighborsClassifier(
        n_neighbors=k
    )

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    accuracies.append(accuracy)

    print(
        "K =", k,
        "Accuracy =", accuracy
    )


# 4. Find Best K

best_index = accuracies.index(
    max(accuracies)
)

best_k = list(k_values)[best_index]

best_accuracy = accuracies[best_index]


print("BEST K VALUE")

print("Best K:", best_k)
print("Best Accuracy:", best_accuracy)


# 5. Visualization

plt.figure(figsize=(8, 5))

plt.plot(
    list(k_values),
    accuracies,
    marker="o"
)

plt.title("KNN Accuracy for Different K Values")
plt.xlabel("K Value")
plt.ylabel("Accuracy")

plt.xticks(list(k_values))

plt.grid(True)

plt.show()


# 6. Train Final Model

final_model = KNeighborsClassifier(
    n_neighbors=best_k
)

final_model.fit(X_train, y_train)

final_prediction = final_model.predict(X_test)

final_accuracy = accuracy_score(
    y_test,
    final_prediction
)


print("\nFinal Model Accuracy:")
print(final_accuracy)


print("DAY 22 COMPLETED")
