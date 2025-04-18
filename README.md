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

