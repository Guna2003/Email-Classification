from flask import Flask, request, render_template
import joblib
from utils import mask_pii
import os

app = Flask(__name__)

# Load model from root
model_path = os.path.join(os.getcwd(), 'email_classifier.pkl')
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
