import os
import gdown
import joblib

MODEL_PATH = "email_classifier.pkl"
FILE_ID = "1Ds0FbGNO30S3e8F3GZIG_LOCEie5dqy0" 


if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)


model = joblib.load(MODEL_PATH)
