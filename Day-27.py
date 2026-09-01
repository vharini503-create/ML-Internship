# ==========================================
# DAY 27 - BOOSTING
# GRADIENT BOOSTING & ADABOOST
# ==========================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.ensemble import (
    GradientBoostingClassifier,
    AdaBoostClassifier
)

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


print("DAY 27 - BOOSTING")


# ------------------------------------------
# 1. Load Iris Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:")
print(X.shape)

print("\nTarget Classes:")
print(iris.target_names)


# ------------------------------------------
# 2. Train-Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:")
print(len(X_train))

print("\nTesting Samples:")
print(len(X_test))


# ==========================================
# 3. GRADIENT BOOSTING
# ==========================================

gradient_model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)


# Train

gradient_model.fit(
    X_train,
    y_train
)

print("\nGradient Boosting Model Trained!")


# Prediction

gradient_prediction = gradient_model.predict(
    X_test
)


# Accuracy

gradient_accuracy = accuracy_score(
    y_test,
    gradient_prediction
)

print("\nGradient Boosting Accuracy:")
print(gradient_accuracy)


# Confusion Matrix

print("\nGradient Boosting Confusion Matrix:")

print(
    confusion_matrix(
        y_test,
        gradient_prediction
    )
)


# ==========================================
# 4. ADABOOST
# ==========================================

ada_model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(
        max_depth=1,
        random_state=42
    ),
    n_estimators=100,
    random_state=42
)


# Train

ada_model.fit(
    X_train,
    y_train
)

print("\nAdaBoost Model Trained!")


# Prediction

ada_prediction = ada_model.predict(
    X_test
)


# Accuracy

ada_accuracy = accuracy_score(
    y_test,
    ada_prediction
)

print("\nAdaBoost Accuracy:")
print(ada_accuracy)


# Confusion Matrix

print("\nAdaBoost Confusion Matrix:")

print(
    confusion_matrix(
        y_test,
        ada_prediction
    )
)


# ==========================================
# 5. CLASSIFICATION REPORT
# ==========================================

print("GRADIENT BOOSTING REPORT")

print(
    classification_report(
        y_test,
        gradient_prediction
    )
)


print("ADABOOST REPORT")

print(
    classification_report(
        y_test,
        ada_prediction
    )
)


# ==========================================
# 6. COMPARE MODELS
# ==========================================

print("MODEL COMPARISON")

print(
    "Gradient Boosting Accuracy:",
    gradient_accuracy
)

print(
    "AdaBoost Accuracy:",
    ada_accuracy
)


if gradient_accuracy > ada_accuracy:

    print("\nBetter Accuracy: Gradient Boosting")

elif ada_accuracy > gradient_accuracy:

    print("\nBetter Accuracy: AdaBoost")

else:

    print("\nBoth models have the same accuracy.")


# ==========================================
# 7. TEST DIFFERENT LEARNING RATES
# ==========================================

print("LEARNING RATE COMPARISON")

for rate in [0.01, 0.05, 0.1, 0.2]:

    model = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=rate,
        max_depth=3,
        random_state=42
    )

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

    print(
        "Learning Rate:",
        rate,
        "| Accuracy:",
        accuracy
    )


print("DAY 27 COMPLETED")
