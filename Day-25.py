# DAY 25 - END-TO-END ML MINI PROJECT
# STUDENT PERFORMANCE PREDICTION

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

import joblib


print("STUDENT PERFORMANCE PREDICTION")


# 1. CREATE DATASET

data = {
    "Age": [
        18, 19, 20, 21, 18,
        22, 19, 20, 21, 18,
        23, 20, 19, 22, 21,
        18, 20, 23, 19, 22
    ],

    "Study_Hours": [
        2, 5, 6, 3, 8,
        7, 4, 6, 2, 9,
        3, 7, 5, 8, 4,
        6, 2, 9, 5, 7
    ],

    "Attendance": [
        65, 80, 85, 70, 92,
        88, 75, 90, 60, 95,
        68, 86, 78, 94, 72,
        84, 62, 96, 79, 89
    ],

    "Previous_Score": [
        55, 72, 80, 60, 88,
        82, 68, 85, 50, 91,
        58, 83, 70, 90, 65,
        77, 52, 94, 73, 87
    ],

    "Gender": [
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],

    "Passed": [
        0, 1, 1, 0, 1,
        1, 1, 1, 0, 1,
        0, 1, 1, 1, 0,
        1, 0, 1, 1, 1
    ]
}


df = pd.DataFrame(data)


# 2. UNDERSTAND THE DATA

print("\nDataset:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 3. CHECK MISSING VALUES

print("\nMissing Values:")
print(df.isnull().sum())


# 4. ENCODE CATEGORICAL DATA

df["Gender"] = df["Gender"].map({
    "Female": 0,
    "Male": 1
})

print("\nAfter Encoding Gender:")
print(df.head())


# 5. SELECT FEATURES AND TARGET

X = df[
    [
        "Age",
        "Study_Hours",
        "Attendance",
        "Previous_Score",
        "Gender"
    ]
]

y = df["Passed"]


print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# 6. TRAIN-TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining Samples:")
print(len(X_train))

print("\nTesting Samples:")
print(len(X_test))


# 7. FEATURE SCALING

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


print("\nFeature Scaling Completed!")


# 8. CREATE MACHINE LEARNING MODEL

model = LogisticRegression()


# 9. TRAIN MODEL

model.fit(
    X_train_scaled,
    y_train
)

print("\nModel Training Completed!")

# 10. MAKE PREDICTIONS

y_pred = model.predict(
    X_test_scaled
)


print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)


# 11. MODEL EVALUATION

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)


print("MODEL EVALUATION")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

# 12. CONFUSION MATRIX

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)


# 13. CLASSIFICATION REPORT

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# 14. PREDICT A NEW STUDENT

new_student = pd.DataFrame({
    "Age": [20],
    "Study_Hours": [7],
    "Attendance": [88],
    "Previous_Score": [82],
    "Gender": [1]
})


# Scale new student's data

new_student_scaled = scaler.transform(
    new_student
)


# Prediction

prediction = model.predict(
    new_student_scaled
)


print("NEW STUDENT PREDICTION")

if prediction[0] == 1:
    print("Prediction: Student is likely to PASS")
else:
    print("Prediction: Student is likely to FAIL")


# 15. SAVE MODEL

joblib.dump(
    model,
    "student_model.pkl"
)

joblib.dump(
    scaler,
    "student_scaler.pkl"
)

print("\nModel saved successfully!")


print("DAY 25 PROJECT COMPLETED")
