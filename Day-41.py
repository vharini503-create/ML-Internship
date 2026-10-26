
# Day 41 - Transfer Learning with MobileNetV2

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.utils import load_img, img_to_array

# Step 1: Load a pretrained model
print("Loading pretrained MobileNetV2 model...")

model = MobileNetV2(
    weights="imagenet",
    include_top=True
)

print("Model loaded successfully!")

# Step 2: Display model information
print("\nModel Information")
print("-----------------")
print("Model name:", model.name)
print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)

# Step 3: Load a sample image
# TensorFlow downloads this sample image from its public repository.
image_url = (
    "https://storage.googleapis.com/"
    "download.tensorflow.org/example_images/grace_hopper.jpg"
)

image_path = tf.keras.utils.get_file(
    "grace_hopper.jpg",
    image_url
)

image = load_img(image_path, target_size=(224, 224))
image_array = img_to_array(image)

# Step 4: Prepare the image for prediction
image_array = np.expand_dims(image_array, axis=0)
image_array = preprocess_input(image_array)

print("\nImage prepared for prediction.")
print("Image tensor shape:", image_array.shape)

# Step 5: Predict the image class
predictions = model.predict(image_array, verbose=0)
top_predictions = decode_predictions(predictions, top=3)[0]

print("\nTop 3 Predictions")
print("-----------------")

for _, label, score in top_predictions:
    print(f"{label}: {score * 100:.2f}%")

# Step 6: Display the sample image
plt.imshow(image)
plt.title("Image Used for Transfer Learning")
plt.axis("off")
plt.tight_layout()
plt.show()

print("\nDay 41 task completed successfully!")
