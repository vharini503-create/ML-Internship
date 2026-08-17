from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("---------- DAY 23 - RANDOM FOREST ---------")

# 1. Load Iris Dataset

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:")
print(X.shape)

print("\nFeature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)

# 2. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# 3. Create Random Forest Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 4. Train the Model

model.fit(X_train, y_train)

print("\nRandom Forest Model Trained Successfully!")

# 5. Make Predictions

y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test)

print("\nPredicted Values:")
print(y_pred)

# 6. Accuracy

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy Score:")
print(accuracy)

# 7. Confusion Matrix

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)

# 8. Classification Report

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# 9. Feature Importance

print("\nFeature Importance:")

for feature, importance in zip(
    iris.feature_names,
    model.feature_importances_
):
    print(feature, ":", importance)


# 10. Predict a New Flower

new_flower = [[
    5.1,
    3.5,
    1.4,
    0.2
]]

prediction = model.predict(new_flower)

print("\nPrediction for New Flower:")

print(iris.target_names[prediction[0]])


print("---------- DAY 23 COMPLETED ----------")
