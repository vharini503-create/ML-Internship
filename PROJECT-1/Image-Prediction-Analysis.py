
# Project 1: Image Classification
#  Prediction and Analysis

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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
# Step 2: Define Prediction Function
# ------------------------------------------

def predict_image(image_path):

    image = load_img(
        image_path,
        target_size=(224, 224)
    )

    image_array = img_to_array(image)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    image_array = preprocess_input(image_array)

    predictions = model.predict(
        image_array,
        verbose=0
    )

    results = decode_predictions(
        predictions,
        top=5
    )[0]

    return image, results

# ------------------------------------------
# Step 3: Read Images
# ------------------------------------------

image_folder = "images"

image_files = [
    file for file in os.listdir(image_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

if not image_files:
    print("Please add images to the images folder.")
    exit()

# ------------------------------------------
# Step 4: Predict and Analyze Images
# ------------------------------------------

prediction_data = []

for image_file in image_files:

    image_path = os.path.join(
        image_folder,
        image_file
    )

    print("\nImage:", image_file)

    image, predictions = predict_image(image_path)

    predicted_label = predictions[0][1]
    confidence = predictions[0][2] * 100

    print("Predicted Class:", predicted_label)
    print("Confidence:", round(confidence, 2), "%")

    print("\nTop 5 Predictions:")

    for _, label, score in predictions:
        print(f"{label}: {score * 100:.2f}%")

    # Save prediction details
    prediction_data.append({
        "Image": image_file,
        "Predicted Class": predicted_label,
        "Confidence (%)": round(confidence, 2)
    })

    # Display image
    plt.figure(figsize=(6, 5))

    plt.imshow(image)

    plt.title(
        f"{predicted_label}\nConfidence: {confidence:.2f}%"
    )

    plt.axis("off")
    plt.tight_layout()
    plt.show()

# ------------------------------------------
# Step 5: Create Prediction Report
# ------------------------------------------

df = pd.DataFrame(prediction_data)

df.to_csv(
    "prediction_results.csv",
    index=False
)

print("\nPrediction Report")
print("----------------")

print(df)

print("\nResults saved to prediction_results.csv")

print("\n Completed Successfully!")
