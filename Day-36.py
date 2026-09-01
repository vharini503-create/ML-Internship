# ==========================================
# DAY 36 - INTRODUCTION TO DEEP LEARNING
# NEURAL NETWORK
# ==========================================

import numpy as np
import tensorflow as tf

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


print("==========================================")
print("DAY 36 - NEURAL NETWORK")
print("==========================================")


# ------------------------------------------
# 1. Load Iris Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Shape:")
print(X.shape)

print("\nNumber of Classes:")
print(len(np.unique(y)))


# ------------------------------------------
# 2. Split Dataset
# ------------------------------------------

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


# ------------------------------------------
# 3. Feature Scaling
# ------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ------------------------------------------
# 4. Create Neural Network
# ------------------------------------------

model = Sequential([

    Dense(
        16,
        activation="relu",
        input_shape=(4,)
    ),

    Dense(
        8,
        activation="relu"
    ),

    Dense(
        3,
        activation="softmax"
    )
])


# ------------------------------------------
# 5. Display Model
# ------------------------------------------

print("\n==========================================")
print("NEURAL NETWORK STRUCTURE")
print("==========================================")

model.summary()


# ------------------------------------------
# 6. Compile Model
# ------------------------------------------

model.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=["accuracy"]
)


# ------------------------------------------
# 7. Train Model
# ------------------------------------------

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


# ------------------------------------------
# 8. Evaluate Model
# ------------------------------------------

print("\n==========================================")
print("MODEL EVALUATION")
print("==========================================")


loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)


print("\nTest Loss:")
print(loss)

print("\nTest Accuracy:")
print(accuracy)


# ------------------------------------------
# 9. Make Predictions
# ------------------------------------------

print("\n==========================================")
print("PREDICTIONS")
print("==========================================")


predictions = model.predict(
    X_test,
    verbose=0
)


predicted_classes = np.argmax(
    predictions,
    axis=1
)


print("\nActual Classes:")
print(y_test)

print("\nPredicted Classes:")
print(predicted_classes)


# ------------------------------------------
# 10. Predict One Sample
# ------------------------------------------

sample = X_test[0].reshape(1, -1)

prediction = model.predict(
    sample,
    verbose=0
)


predicted_class = np.argmax(
    prediction
)


print("\n==========================================")
print("SINGLE SAMPLE PREDICTION")
print("==========================================")

print("Predicted Class:")
print(predicted_class)

print("\nActual Class:")
print(y_test[0])


print("\n==========================================")
print("DAY 36 COMPLETED")
print("==========================================")