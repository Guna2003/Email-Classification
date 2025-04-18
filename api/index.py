from flask import Flask, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

@app.route('/classify_email', methods=['POST'])
def classify_email():
    # Your existing classification logic here
    data = request.get_json()
    email_text = data.get('email_text')

    # Dummy response for example
    response = {
        "category": "Billing",
        "masked_text": "Hello, [NAME]. Your email is [EMAIL].",
        "entities": [
            {"label": "NAME", "entity": "John Doe", "start": 7, "end": 16},
            {"label": "EMAIL", "entity": "john.doe@example.com", "start": 25, "end": 48}
        ]
    }

    return jsonify(response)

# Required for serverless deployment to work properly
if __name__ == "__main__":
    app.run()

