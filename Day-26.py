import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix


print("---------- DAY 26 - SUPPORT VECTOR MACHINE ----------")

# 1. Create Dataset

X, y = make_moons(
    n_samples=300,
    noise=0.2,
    random_state=0
)

print("\nDataset Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

# 2. Visualize Original Dataset

plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y
)

plt.title("Make Moons Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()

# 3. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=0
)

print("\nTraining Samples:")
print(len(X_train))

print("\nTesting Samples:")
print(len(X_test))

# 4. Create SVM Model

svm_model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)

# 5. Train Model

svm_model.fit(
    X_train,
    y_train
)

print("\nSVM Model Trained Successfully!")

# 6. Make Predictions

y_pred = svm_model.predict(
    X_test
)

print("\nActual Values:")
print(y_test)

print("\nPredicted Values:")
print(y_pred)

# 7. Accuracy

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nTest Accuracy:")
print(accuracy)

# 8. Confusion Matrix

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)

# 9. Support Vectors

print("\nNumber of Support Vectors:")

print(svm_model.n_support_)

print("\nTotal Support Vectors:")

print(sum(svm_model.n_support_))

# 10. Try Different C Values

print("TESTING DIFFERENT C VALUES")

for C_value in [0.1, 1, 10, 100]:

    model = SVC(
        kernel="rbf",
        C=C_value,
        gamma="scale"
    )

    model.fit(
        X_train,
        y_train
    )

    prediction = model.predict(
        X_test
    )

    score = accuracy_score(
        y_test,
        prediction
    )

    print(
        "C =", C_value,
        "| Accuracy =", score
    )

# 11. Try Different Gamma Values

print("TESTING DIFFERENT GAMMA VALUES")

for gamma_value in [0.1, 0.5, 1, 5]:

    model = SVC(
        kernel="rbf",
        C=1.0,
        gamma=gamma_value
    )

    model.fit(
        X_train,
        y_train
    )

    prediction = model.predict(
        X_test
    )

    score = accuracy_score(
        y_test,
        prediction
    )

    print(
        "Gamma =", gamma_value,
        "| Accuracy =", score
    )


print("---------- DAY 26 COMPLETED ----------")