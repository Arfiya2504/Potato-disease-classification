from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
import os

BUCKET_NAME = "tf-models-arfiya"
MODEL_PATH = "/tmp/potatoes.h5"
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

model = None

def download_blob(bucket_name, source_blob_name, destination_file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def load_model():
    global model
    if model is None:
        if not os.path.exists(MODEL_PATH):
            download_blob(BUCKET_NAME, "models/potatoes.h5", MODEL_PATH)
        model = tf.keras.models.load_model(MODEL_PATH)

def predict(request):
    load_model()

    if request.method != 'POST':
        return {"error": "Only POST allowed"}, 405

    file = request.files.get("file")
    if file is None:
        return {"error": "No file uploaded"}, 400

    try:
        image = Image.open(file).convert("RGB").resize((256, 256))
        image_array = np.array(image) / 255.0
        img_tensor = tf.expand_dims(image_array, 0)

        predictions = model.predict(img_tensor)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = float(round(100 * np.max(predictions[0]), 2))

        return {
            "class": predicted_class,
            "confidence": confidence
        }

    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}, 500
