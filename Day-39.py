# ==========================================
# DAY 39 - CNN IMPROVEMENT
# DATA AUGMENTATION AND DROPOUT
# ==========================================

import tensorflow as tf

from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

from tensorflow.keras.preprocessing.image import ImageDataGenerator


print("==========================================")
print("DAY 39 - CNN IMPROVEMENT")
print("==========================================")


# 1. Load MNIST Dataset

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# 2. Normalize Pixel Values

X_train = X_train / 255.0
X_test = X_test / 255.0


# 3. Add Channel Dimension

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

print("After Reshaping:", X_train.shape)


# 4. Data Augmentation

datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1
)


# 5. Create CNN Model

model = Sequential([

    Input(shape=(28, 28, 1)),

    # First Convolution
    Conv2D(
        32,
        (3, 3),
        activation="relu"
    ),

    MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Second Convolution
    Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),

    MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Flatten
    Flatten(),

    # Dense Layer
    Dense(
        128,
        activation="relu"
    ),

    # Dropout
    Dropout(0.5),

    # Output Layer
    Dense(
        10,
        activation="softmax"
    )
])


# 6. Display Model

print("\n==========================================")
print("MODEL STRUCTURE")
print("==========================================")

model.summary()


# 7. Compile Model

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# 8. Train Model

print("\n==========================================")
print("TRAINING MODEL")
print("==========================================")

history = model.fit(
    datagen.flow(
        X_train,
        y_train,
        batch_size=64
    ),
    epochs=5,
    validation_data=(X_test, y_test)
)


# 9. Evaluate Model

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


# 10. Make Predictions

predictions = model.predict(
    X_test[:10],
    verbose=0
)

predicted_classes = tf.argmax(
    predictions,
    axis=1
).numpy()


# 11. Display Predictions

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
print("DAY 39 COMPLETED")
print("==========================================")