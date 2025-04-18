Email Classification for Support Team
This project is a web-based application designed to help customer support teams automatically classify incoming emails and mask sensitive Personally Identifiable Information (PII). It uses Natural Language Processing (NLP) and Machine Learning (ML) to achieve this.

Features
Classifies emails into predefined categories (e.g., billing, technical support, general query, etc.)

Masks PII like emails, phone numbers, names, etc.

Displays detected entities with their type and position

User-friendly web interface built using HTML and Flask

Supports POST requests for API integration

Tech Stack
Frontend: HTML, CSS (custom styled)

Backend: Python, Flask

NLP & ML: spaCy, scikit-learn, pandas, re

Model: Random Forest with TF-IDF pipeline

Deployment: Flask local server (http://127.0.0.1:5000)

Project Structure:
email_classification/
│
├── app.py                # Main Flask application
├── models.py             # ML model loading and classification logic
├── utils.py              # PII masking and entity extraction logic
├── templates/
│   └── index.html        # Frontend HTML template
├── static/              
├── emails.csv            # Dataset with email and type columns
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

How to Run
Clone the repository
Create and activate a virtual environment
Install dependencies:
bash
pip install -r requirements.txt
Run the app:
bash
python app.py
Open in browser:
http://127.0.0.1:5000


API Endpoint
URL: /classify_email

Method: POST

Input: email_text (as form data or JSON)

Output: JSON response with category, masked_text, and entities

Example Input:
{
  "email_text": "Hi, my name is John Doe. My email is john.doe@example.com. Please check the billing error."
}

Example Output:

{
  "category": "Billing",
  "masked_text": "Hi, my name is [NAME]. My email is [EMAIL]. Please check the billing error.",
  "entities": [
    {
      "label": "EMAIL",
      "entity": "john.doe@example.com",
      "start": 30,
      "end": 50
    },
    {
      "label": "NAME",
      "entity": "John Doe",
      "start": 17,
      "end": 25
    }
  ]
}

Dataset
The dataset used is a CSV file (emails.csv) containing:

email column: text content of the email

type column: category label for classification