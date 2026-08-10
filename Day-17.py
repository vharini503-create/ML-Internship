import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("----- DAY 17 - MACHINE LEARNING -----")

# 1. Create Dataset

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 45, 50, 55, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

# 2. Features and Target

X = df[["Study_Hours"]]
y = df["Marks"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# 3. Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

# 4. Create Model

model = LinearRegression()

# 5. Train Model

model.fit(X_train, y_train)

print("\nModel trained successfully!")

# 6. Make Predictions

predictions = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(predictions)

# 7. Evaluate Model

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# 8. Predict New Data

new_hours = [[7]]

predicted_marks = model.predict(new_hours)

print("\nPredicted marks for 7 study hours:",
      predicted_marks[0])


print("\n----- DAY 17 COMPLETED -----")