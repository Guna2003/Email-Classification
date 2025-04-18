import os
import gdown
import joblib
from flask import Flask, request, render_template
from utils import mask_pii

app = Flask(__name__)

# Google Drive file ID for the model
file_id = '1Ds0FbGNO30S3e8F3GZIG_LOCEie5dqy0'  # Replace this with your actual Google Drive file ID
model_path = 'email_classifier.pkl'

# Check if the model exists in the local directory; if not, download it
if not os.path.exists(model_path):
    print("Downloading model from Google Drive...")
    gdown.download(f'https://drive.google.com/uc?export=download&id={file_id}', model_path, quiet=False)
else:
    print("Model file already exists!")

# Load model from the root
email_classifier_model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_email', methods=['POST'])
def process_email():
    email_text = request.form['email_text']

    # Predict the category
    category = email_classifier_model.predict([email_text])[0]

    # Mask PII
    masked_text, entities = mask_pii(email_text)

    return render_template('index.html', category=category, masked_text=masked_text, entities=entities, original=email_text)

@app.route('/classify_email', methods=['POST'])
def classify_email():
    # This one is for Postman / API call
    data = request.get_json()
    email_text = data.get('email_text', '')

    if not email_text:
        return {"error": "No email_text provided"}, 400

    # Predict the category
    category = email_classifier_model.predict([email_text])[0]

    # Mask PII
    masked_text, entities = mask_pii(email_text)

    return {
        'category': category,
        'masked_text': masked_text,
        'entities': entities,
        'original': email_text
    }


if __name__ == '__main__':
    app.run(debug=True)
