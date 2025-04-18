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

## 📁 Project Structure
email_classification/ │ ├── app.py # Main Flask application ├── models.py # ML model loading and classification logic ├── utils.py # PII masking and entity extraction logic ├── templates/ │ └── index.html # Frontend HTML template ├── static/ # Optional static files ├── emails.csv # Dataset with email and type columns ├── requirements.txt # Python dependencies └── README.md # Project documentation


---

## 🚀 How to Run

1. **Clone the repository**
2. **Create and activate a virtual environment**
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
python app.py
http://127.0.0.1:5000


