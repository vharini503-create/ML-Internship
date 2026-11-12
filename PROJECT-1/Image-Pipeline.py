
# Project 1: Image Classification Using Transfer Learning
# Image Classification Pipeline

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.utils import load_img, img_to_array

# ------------------------------------------
# Step 1: Load Pretrained Model
# ------------------------------------------

print("Loading MobileNetV2...")

model = MobileNetV2(
    weights="imagenet",
    include_top=True
)

print("Model loaded successfully!")

# ------------------------------------------
# Step 2: Create Image Prediction Function
# ------------------------------------------

def predict_image(image_path):

    # Load image
    image = load_img(
        image_path,
        target_size=(224, 224)
    )

    # Convert image into array
    image_array = img_to_array(image)

    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Preprocess image
    image_array = preprocess_input(image_array)

    # Predict image
    predictions = model.predict(
        image_array,
        verbose=0
    )

    # Decode predictions
    results = decode_predictions(
        predictions,
        top=3
    )[0]

    return image, results

# ------------------------------------------
# Step 3: Load Images from Folder
# ------------------------------------------

image_folder = "images"

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

image_files = [
    file for file in os.listdir(image_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Download sample image if folder is empty
if len(image_files) == 0:

    print("No images found. Downloading sample image...")

    sample_url = (
        "https://storage.googleapis.com/"
        "download.tensorflow.org/example_images/grace_hopper.jpg"
    )

    sample_path = tf.keras.utils.get_file(
        "grace_hopper.jpg",
        sample_url
    )

    image_files = [sample_path]

    image_folder = ""

# ------------------------------------------
# Step 4: Predict Multiple Images
# ------------------------------------------

for image_file in image_files:

    if image_folder:
        image_path = os.path.join(
            image_folder,
            image_file
        )
    else:
        image_path = image_file

    print("\nImage:", image_file)

    image, predictions = predict_image(image_path)

    print("Top 3 Predictions:")

    for _, label, confidence in predictions:
        print(
            f"{label}: {confidence * 100:.2f}%"
        )

    # --------------------------------------
    # Step 5: Display Prediction
    # --------------------------------------

    best_label = predictions[0][1]
    best_confidence = predictions[0][2] * 100

    plt.figure(figsize=(6, 5))

    plt.imshow(image)

    plt.title(
        f"{best_label} ({best_confidence:.2f}%)"
    )

    plt.axis("off")
    plt.tight_layout()
    plt.show()

print("\n Completed Successfully!")
