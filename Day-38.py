# ==========================================
# DAY 38 - CONVOLUTIONAL NEURAL NETWORK
# ==========================================

import numpy as np
import tensorflow as tf

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense


print("==========================================")
print("DAY 38 - CNN IMAGE CLASSIFICATION")
print("==========================================")


# 1. Load MNIST Dataset

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# 2. Normalize Pixel Values

X_train = X_train / 255.0
X_test = X_test / 255.0


# 3. Add Channel Dimension

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

print("New Training Shape:", X_train.shape)


# 4. Create CNN Model

model = Sequential([

    # Convolution Layer
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(28, 28, 1)
    ),

    # Pooling Layer
    MaxPooling2D(pool_size=(2, 2)),

    # Second Convolution Layer
    Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),

    # Second Pooling Layer
    MaxPooling2D(pool_size=(2, 2)),

    # Convert feature maps into one dimension
    Flatten(),

    # Fully connected layer
    Dense(64, activation="relu"),

    # Output layer - 10 digits
    Dense(10, activation="softmax")
])


# 5. Display Model

print("\n==========================================")
print("CNN MODEL STRUCTURE")
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
print("TRAINING CNN")
print("==========================================")

history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
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
    X_test[:10],
    verbose=0
)

predicted_classes = np.argmax(
    predictions,
    axis=1
)


# 10. Display Predictions

print("\n==========================================")
print("PREDICTIONS")
print("==========================================")

for i in range(10):

    print(
        "Actual:",
        y_test[i],
        "| Predicted:",
        predicted_classes[i]
    )


print("\n==========================================")
print("DAY 38 COMPLETED")
print("==========================================")