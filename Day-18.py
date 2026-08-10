import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


print("----- DAY 18 - LINEAR REGRESSION -----")

# 1. Create Dataset

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 42, 48, 55, 60, 65, 70, 78, 85, 92]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

# 2. Separate Features and Target

X = df[["Study_Hours"]]
y = df["Marks"]

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

# 4. Create Linear Regression Model

model = LinearRegression()

# 5. Train Model

model.fit(X_train, y_train)

print("\nModel trained successfully!")

# 6. Make Predictions

y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

# 7. Model Evaluation

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("\n----- MODEL EVALUATION -----")

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# 8. Predict for New Input

hours = [[7]]

prediction = model.predict(hours)

print("\nPredicted marks for 7 study hours:")
print(prediction[0])


print("\n----- DAY 18 COMPLETED -----")