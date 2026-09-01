# ==========================================
# DAY 29 - SPECTRAL CLUSTERING
# ==========================================

import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.cluster import SpectralClustering
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_score



print("DAY 29 - SPECTRAL CLUSTERING")



# ------------------------------------------
# 1. Create Dataset
# ------------------------------------------

X, y = make_moons(
    n_samples=300,
    noise=0.08,
    random_state=42
)

print("\nDataset Shape:")
print(X.shape)


# ------------------------------------------
# 2. Visualize Original Dataset
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1]
)

plt.title("Original Make Moons Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# ------------------------------------------
# 3. Create Spectral Clustering Model
# ------------------------------------------

spectral_model = SpectralClustering(
    n_clusters=2,
    affinity="nearest_neighbors",
    random_state=42
)


# ------------------------------------------
# 4. Perform Clustering
# ------------------------------------------

spectral_labels = spectral_model.fit_predict(X)


print("\nSpectral Clustering Completed!")

print("\nFirst 20 Cluster Labels:")
print(spectral_labels[:20])


# ------------------------------------------
# 5. Visualize Spectral Clustering
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=spectral_labels
)

plt.title("Spectral Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# ------------------------------------------
# 6. Silhouette Score
# ------------------------------------------

spectral_score = silhouette_score(
    X,
    spectral_labels
)

print("\nSpectral Clustering Silhouette Score:")
print(spectral_score)


# ==========================================
# 7. Compare with K-Means
# ==========================================

kmeans = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

kmeans_labels = kmeans.fit_predict(X)


kmeans_score = silhouette_score(
    X,
    kmeans_labels
)



print("MODEL COMPARISON")


print(
    "Spectral Clustering Score:",
    spectral_score
)

print(
    "K-Means Score:",
    kmeans_score
)


# ------------------------------------------
# 8. Visualize K-Means
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=kmeans_labels
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# ------------------------------------------
# 9. Final Result
# ------------------------------------------

if spectral_score > kmeans_score:

    print("\nSpectral Clustering performed better.")

elif kmeans_score > spectral_score:

    print("\nK-Means performed better.")

else:

    print("\nBoth models have the same score.")



print("DAY 29 COMPLETED")
