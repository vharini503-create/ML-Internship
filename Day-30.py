# ==========================================
# DAY 30 - CLASSICAL ML REVIEW
# ==========================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


print("==========================================")
print("DAY 30 - CLASSICAL ML REVIEW")
print("==========================================")


# 1. Load Dataset

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
    random_state=42,
    stratify=y
)


# 3. Feature Scaling

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 4. Create Models

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

    "SVM":
        SVC(kernel="rbf", C=1.0)
}


# 5. Train and Evaluate

results = {}


for name, model in models.items():

    # SVM and Logistic Regression use scaled data
    if name in ["Logistic Regression", "SVM"]:

        model.fit(
            X_train_scaled,
            y_train
        )

        prediction = model.predict(
            X_test_scaled
        )

    else:

        model.fit(
            X_train,
            y_train
        )

        prediction = model.predict(
            X_test
        )


    accuracy = accuracy_score(
        y_test,
        prediction
    )

    results[name] = accuracy

    print("\n------------------------------------------")
    print(name)
    print("------------------------------------------")

    print("Accuracy:", accuracy)

    print("\nConfusion Matrix:")
    print(
        confusion_matrix(
            y_test,
            prediction
        )
    )


# 6. Compare Results

print("\n==========================================")
print("MODEL COMPARISON")
print("==========================================")

for name, accuracy in results.items():

    print(
        name,
        "->",
        accuracy
    )


# 7. Find Best Model

best_model = max(
    results,
    key=results.get
)

print("\nBest Model:")
print(best_model)

print("\nBest Accuracy:")
print(results[best_model])


print("\n==========================================")
print("CLASSICAL ML STAGE COMPLETED")
print("==========================================")