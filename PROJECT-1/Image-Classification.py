
# Project 1: Image Classification Using Transfer Learning


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import load_img, img_to_array

# ------------------------------------------
# Step 1: Load Pretrained MobileNetV2 Model
# ------------------------------------------

print("Loading MobileNetV2 model...")

model = MobileNetV2(
    weights="imagenet",
    include_top=True
)

print("Model loaded successfully!")

# ------------------------------------------
# Step 2: Display Model Information
# ------------------------------------------

print("\nModel Information")
print("----------------")
print("Model Name:", model.name)
print("Input Shape:", model.input_shape)
print("Output Shape:", model.output_shape)

# ------------------------------------------
# Step 3: Download Sample Image
# ------------------------------------------

image_url = (
    "https://storage.googleapis.com/"
    "download.tensorflow.org/example_images/grace_hopper.jpg"
)

image_path = tf.keras.utils.get_file(
    "grace_hopper.jpg",
    image_url
)

# ------------------------------------------
# Step 4: Load and Resize Image
# ------------------------------------------

image = load_img(
    image_path,
    target_size=(224, 224)
)

image_array = img_to_array(image)

# ------------------------------------------
# Step 5: Preprocess Image
# ------------------------------------------

image_array = np.expand_dims(
    image_array,
    axis=0
)

image_array = preprocess_input(image_array)

print("\nImage Shape:", image_array.shape)

# ------------------------------------------
# Step 6: Predict Image Class
# ------------------------------------------

print("\nPredicting image...")

predictions = model.predict(
    image_array,
    verbose=0
)

# ------------------------------------------
# Step 7: Display Top 3 Predictions
# ------------------------------------------

decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(
    predictions,
    top=3
)[0]

print("\nTop 3 Predictions")
print("----------------")

for _, label, confidence in decoded_predictions:
    print(f"{label}: {confidence * 100:.2f}%")

# ------------------------------------------
# Step 8: Display Image
# ------------------------------------------

plt.figure(figsize=(6, 6))

plt.imshow(image)
plt.title("Transfer Learning - Image Classification")
plt.axis("off")

plt.show()

