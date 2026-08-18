import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("DAY 24 - DATA PREPROCESSING")

# 1. Create Sample Dataset

data = {
    "Age": [20, 21, 22, None, 24, 25, 23, 21, None, 26],
    "Study_Hours": [3, 5, 4, 6, None, 8, 7, 4, 5, 9],
    "Gender": [
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],
    "Attendance": [75, 80, 85, 90, 88, None, 92, 78, 84, 95],
    "Passed": [0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# 2. Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# 3. Handle Missing Values

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

df["Study_Hours"] = df["Study_Hours"].fillna(
    df["Study_Hours"].mean()
)

df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

print("\nAfter Handling Missing Values:")
print(df)

# 4. Encode Categorical Data

df["Gender"] = df["Gender"].map({
    "Female": 0,
    "Male": 1
})

print("\nAfter Encoding Gender:")
print(df)

# 5. Feature Selection

X = df[
    ["Age", "Study_Hours", "Gender", "Attendance"]
]

y = df["Passed"]

print("\nSelected Features:")
print(X)

print("\nTarget:")
print(y)

# 6. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

# 7. Feature Scaling

scaler = StandardScaler()

# Fit ONLY on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform testing data
X_test_scaled = scaler.transform(X_test)

print("\nScaled Training Data:")
print(X_train_scaled)

print("\nScaled Testing Data:")
print(X_test_scaled)

# 8. Train ML Model

model = LogisticRegression()

model.fit(
    X_train_scaled,
    y_train
)

print("\nModel Training Completed!")

# 9. Prediction

y_pred = model.predict(
    X_test_scaled
)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)


# 10. Evaluation

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(accuracy)


print("---------- DAY 24 COMPLETED -----------")
