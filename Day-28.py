# ==========================================
# DAY 28 - GAUSSIAN MIXTURE MODEL
# EXPECTATION-MAXIMIZATION
# ==========================================

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture

from sklearn.metrics import silhouette_score


print("DAY 28 - GMM AND EM")



# ------------------------------------------
# 1. Create Sample Dataset
# ------------------------------------------

X, y = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=1.2,
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

plt.title("Original Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# ------------------------------------------
# 3. Create GMM Model
# ------------------------------------------

gmm = GaussianMixture(
    n_components=3,
    random_state=42
)


# ------------------------------------------
# 4. Train GMM
# ------------------------------------------

gmm.fit(X)

print("\nGMM Model Trained Successfully!")


# ------------------------------------------
# 5. Predict Clusters
# ------------------------------------------

clusters = gmm.predict(X)

print("\nCluster Labels:")
print(clusters[:20])


# ------------------------------------------
# 6. Cluster Probabilities
# ------------------------------------------

probabilities = gmm.predict_proba(X)

print("\nCluster Probabilities for First 5 Points:")

print(probabilities[:5])


# ------------------------------------------
# 7. Display Gaussian Means
# ------------------------------------------

print("\nGaussian Means:")

print(gmm.means_)


# ------------------------------------------
# 8. Display Covariances
# ------------------------------------------

print("\nCovariance Matrices:")

print(gmm.covariances_)


# ------------------------------------------
# 9. Visualize GMM Clusters
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=clusters
)

plt.scatter(
    gmm.means_[:, 0],
    gmm.means_[:, 1],
    marker="X",
    s=200
)

plt.title("GMM Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# ------------------------------------------
# 10. Calculate Silhouette Score
# ------------------------------------------

score = silhouette_score(
    X,
    clusters
)

print("\nSilhouette Score:")
print(score)


# ------------------------------------------
# 11. Check Convergence
# ------------------------------------------

print("\nNumber of EM Iterations:")
print(gmm.n_iter_)

print("\nDid EM Converge?")
print(gmm.converged_)


# ------------------------------------------
# 12. Compare Different Number of Components
# ------------------------------------------


print("TESTING DIFFERENT NUMBER OF CLUSTERS")


for k in [2, 3, 4, 5]:

    model = GaussianMixture(
        n_components=k,
        random_state=42
    )

    model.fit(X)

    labels = model.predict(X)

    score = silhouette_score(
        X,
        labels
    )

    print(
        "Clusters:",
        k,
        "| Silhouette Score:",
        score
    )



print("DAY 28 COMPLETED")
