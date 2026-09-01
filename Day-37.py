# ==========================================
# DAY 37 - NEURAL NETWORK TRAINING
# ==========================================

import numpy as np
import tensorflow as tf

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


print("==========================================")
print("DAY 37 - NEURAL NETWORK TRAINING")
print("==========================================")


# 1. Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:", X.shape)
print("Classes:", iris.target_names)


# 2. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 3. Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 4. Create Neural Network
model = Sequential([

    Dense(16, activation="relu", input_shape=(4,)),

    Dense(8, activation="relu"),

    Dense(3, activation="softmax")
])


# 5. Display Model
print("\n==========================================")
print("MODEL STRUCTURE")
print("==========================================")

model.summary()


# 6. Compile Model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# 7. Train Model
print("\n==========================================")
print("TRAINING MODEL")
print("==========================================")

history = model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=8,
    validation_split=0.2,
    verbose=1
)


# 8. Evaluate Model
print("\n==========================================")
print("MODEL EVALUATION")
print("==========================================")

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("Test Loss:", loss)
print("Test Accuracy:", accuracy)


# 9. Make Predictions
predictions = model.predict(
    X_test,
    verbose=0
)

predicted_classes = np.argmax(
    predictions,
    axis=1
)


# 10. Accuracy Score
accuracy_score_value = accuracy_score(
    y_test,
    predicted_classes
)

print("\nAccuracy Score:", accuracy_score_value)


# 11. Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predicted_classes))


# 12. Compare Actual and Predicted
print("\n==========================================")
print("ACTUAL VS PREDICTED")
print("==========================================")

for actual, predicted in zip(
    y_test[:10],
    predicted_classes[:10]
):
    print(
        "Actual:",
        iris.target_names[actual],
        "| Predicted:",
        iris.target_names[predicted]
    )


print("\n==========================================")
print("DAY 37 COMPLETED")
print("==========================================")