from flask import Flask, request, render_template
import joblib
import spacy
from utils import mask_pii

app = Flask(__name__)

email_classifier_model = joblib.load("email_classifier.pkl")
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_email', methods=['POST'])
def process_email():
    email_text = request.form['email_text']
    category = email_classifier_model.predict([email_text])[0]
    masked_text, entities = mask_pii(email_text)
    return render_template(
    'index.html',
    category=category,
    masked_text=masked_text,
    entities=entities if entities else [],
    email_text=email_text
)



@app.route('/classify_email', methods=['POST'])
def classify_email():
    data = request.get_json()
    email_text = data.get('email_text', '')
    if not email_text:
        return {"error": "No email_text provided"}, 400
    category = email_classifier_model.predict([email_text])[0]
    masked_text, entities = mask_pii(email_text)
    return {
        'category': category,
        'masked_text': masked_text,
        'entities': entities,
        'original': email_text
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7860)
