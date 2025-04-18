# Email Classification for Support Team

This project is a web-based application designed to help customer support teams automatically classify incoming emails and mask sensitive Personally Identifiable Information (PII). It uses Natural Language Processing (NLP) and Machine Learning (ML) to achieve this.

---

## 🔧 Features

- Classifies emails into predefined categories (e.g., billing, technical support, general query, etc.)
- Masks PII like emails, phone numbers, names, etc.
- Displays detected entities with their type and position
- User-friendly web interface built using HTML and Flask
- Supports POST requests for API integration

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (custom styled)
- **Backend:** Python, Flask
- **NLP & ML:** spaCy, scikit-learn, pandas, re
- **Model:** Random Forest with TF-IDF pipeline
- **Deployment:** Flask local server (`http://127.0.0.1:5000`)

---

<pre><code>## 📁 Project Structure ``` email_classification/ ├── app.py # Main Flask application ├── models.py # ML model loading and classification logic ├── utils.py # PII masking and entity extraction logic ├── templates/ │ └── index.html # Frontend HTML template ├── static/ # Optional static files ├── emails.csv # Dataset with email and type columns ├── requirements.txt # Python dependencies └── README.md # Project documentation ``` </code></pre>


---

## 🚀 How to Run

1. **Clone the repository**
2. **Create and activate a virtual environment**
3. **Install dependencies:**
4. **pip install -r dependies:**
5. **python app.py**
6. **http://127.0.0.1:500**

## 📡 API Endpoint

1. URL: /classify_email
2. Method: POST
3. Input: email_text (sent as JSON or form data)
4. Response: JSON containing:
5. category — predicted category
6. masked_text — email with PII replaced
7. entities — list of detected PII with type and position

## 🧪 Sample Input
-json

-{
  "email_text": "Hi, my name is John Doe. My email is john.doe@example.com. Please check the billing error."
}

## 📤 Sample Output
-json

-{
  -"category": "Billing",
  -"masked_text": "Hi, my name is [NAME]. My email is [EMAIL]. Please check the billing error.",
  -"entities": [
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





