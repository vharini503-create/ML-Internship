
# ==========================================
# DAY 40 - CNN EVALUATION AND VISUALIZATION
# ==========================================

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Input, Conv2D, MaxPooling2D, Flatten, Dense
)

print("DAY 40 - CNN EVALUATION AND VISUALIZATION")

# 1. Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = (
    tf.keras.datasets.mnist.load_data()
)

# 2. Normalize pixel values
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# 3. Add the channel dimension
X_train = X_train[..., np.newaxis]
X_test = X_test[..., np.newaxis]

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# 4. Create the CNN model
model = Sequential([
    Input(shape=(28, 28, 1)),

    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

# 5. Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# 6. Train the model
print("\nTraining CNN...")

model.fit(
    X_train,
    y_train,
    epochs=3,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

# 7. Evaluate the model
test_loss, test_accuracy = model.evaluate(
    X_test, y_test, verbose=0
)

print("\nTest Loss:", round(test_loss, 4))
print("Test Accuracy:", round(test_accuracy * 100, 2), "%")

# 8. Predict the first 10 test images
probabilities = model.predict(X_test[:10], verbose=0)

predictions = np.argmax(probabilities, axis=1)
actual_labels = y_test[:10]

# 9. Display predictions
print("\nPREDICTION RESULTS")

for i in range(10):
    print(
        f"Image {i + 1}: "
        f"Actual = {actual_labels[i]}, "
        f"Predicted = {predictions[i]}"
    )

# 10. Visualize the images and predictions
plt.figure(figsize=(12, 5))

for i in range(10):
    plt.subplot(2, 5, i + 1)

    plt.imshow(X_test[i].squeeze(), cmap="gray")

    predicted = predictions[i]
    actual = actual_labels[i]

    if predicted == actual:
        title_color = "green"
    else:
        title_color = "red"

    plt.title(
        f"Actual: {actual}\nPredicted: {predicted}",
        color=title_color
    )

    plt.axis("off")

plt.suptitle("CNN Handwritten Digit Predictions")
plt.tight_layout()
plt.show()

# 11. Identify incorrect predictions
wrong_indices = np.where(
    predictions != actual_labels
)[0]

print("\nIncorrect predictions among first 10 images:")

if len(wrong_indices) == 0:
    print("All 10 predictions are correct!")
else:
    for index in wrong_indices:
        print(
            f"Image {index + 1}: "
            f"Actual = {actual_labels[index]}, "
            f"Predicted = {predictions[index]}"
        )

print("\nDAY 40 COMPLETED")
