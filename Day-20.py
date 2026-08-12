import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.cluster import KMeans

from sklearn.metrics import accuracy_score


print("---------- DAY 20 - MACHINE LEARNING ALGORITHMS ----------")


# PART 1 - LOAD IRIS DATASET

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:")
print(X.shape)

print("\nFeature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)


# PART 2 - TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# PART 3 - DECISION TREE

print("DECISION TREE")


decision_tree = DecisionTreeClassifier(
    random_state=42
)

decision_tree.fit(X_train, y_train)

tree_prediction = decision_tree.predict(X_test)

tree_accuracy = accuracy_score(
    y_test,
    tree_prediction
)

print("\nActual Values:")
print(y_test)

print("\nPredicted Values:")
print(tree_prediction)

print("\nDecision Tree Accuracy:")
print(tree_accuracy)


# PART 4 - KNN

print("K-NEAREST NEIGHBORS")


knn = KNeighborsClassifier(
    n_neighbors=5
)

knn.fit(X_train, y_train)

knn_prediction = knn.predict(X_test)

knn_accuracy = accuracy_score(
    y_test,
    knn_prediction
)

print("\nKNN Accuracy:")
print(knn_accuracy)


# PART 5 - MODEL COMPARISON

comparison = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "KNN"
    ],
    "Accuracy": [
        tree_accuracy,
        knn_accuracy
    ]
})

print("MODEL COMPARISON")

print(comparison)


# PART 6 - K-MEANS CLUSTERING

print("K-MEANS CLUSTERING")


kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(X)

clusters = kmeans.labels_

print("\nCluster Labels:")
print(clusters)


# Create DataFrame

cluster_df = pd.DataFrame(
    X,
    columns=iris.feature_names
)

cluster_df["Cluster"] = clusters

print("\nClustered Data:")
print(cluster_df.head())


# PART 7 - K-MEANS VISUALIZATION

plt.figure(figsize=(7, 5))

plt.scatter(
    cluster_df["sepal length (cm)"],
    cluster_df["petal length (cm)"],
    c=cluster_df["Cluster"]
)

plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.show()


# FINAL SUMMARY

print("FINAL RESULTS")

print("Decision Tree Accuracy:", tree_accuracy)
print("KNN Accuracy:", knn_accuracy)

print("\nK-Means Clustering Completed")

print("---------- DAY 20 COMPLETED ----------")
