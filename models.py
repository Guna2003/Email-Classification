import joblib

# Load your pre-trained email classification model
try:
    email_classifier_model = joblib.load('email_classifier.pkl')  # Ensure the correct file path
except Exception as e:
    print(f"Error loading the model: {e}")
