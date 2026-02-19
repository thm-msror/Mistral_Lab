from flask import Flask, request, jsonify
from flask_cors import CORS
from helper import mistral
import json
import os

app = Flask(__name__)
CORS(app)   # ✅ Now app exists

@app.route("/")
def home():
    return "Customer Support Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")
        task = data.get("task", "response")
        user_name = data.get("name", "Customer")

        # ===============================
        # CLASSIFICATION
        # ===============================
        if task == "classification":

            prompt = f"""
You are a bank customer service bot.

Categorize the inquiry into one of the following:
- card arrival
- change pin
- exchange rate
- country support
- cancel transfer
- charge dispute
- customer service

Respond with only the category.

Inquiry: {user_message}
Category:
"""

            result = mistral(prompt)
            return jsonify({"response": result})

        # ===============================
        # EXTRACTION (REAL JSON MODE)
        # ===============================
        elif task == "extract":

            prompt = f"""
Extract structured information from the medical notes below.

Return ONLY valid JSON using this schema:

{{
"age": integer,
"gender": "male" | "female" | "other",
"diagnosis": "migraine" | "diabetes" | "arthritis" | "acne",
"weight": integer,
"smoking": "yes" | "no"
}}

Medical Notes:
{user_message}
"""

            result = mistral(prompt, is_json=True)

            # Convert string JSON to Python dictionary
            parsed_json = json.loads(result)

            return jsonify(parsed_json)

        # ===============================
        # SUMMARIZE
        # ===============================
        elif task == "summarize":

            prompt = f"""
Summarize the following text clearly and concisely:

{user_message}
"""

            result = mistral(prompt)
            return jsonify({"response": result})

        # ===============================
        # PERSONALIZED RESPONSE
        # ===============================
        elif task == "personalized":

            prompt = f"""
You are a professional bank customer support assistant.

Address the customer by their name: {user_name}

Respond clearly, professionally, and politely.

Customer Inquiry:
{user_message}

Sign the message as:
Bank Customer Support
"""

            result = mistral(prompt)
            return jsonify({"response": result})

        # ===============================
        # GENERAL RESPONSE
        # ===============================
        else:

            prompt = f"""
You are a helpful customer service assistant.
Respond professionally and clearly:

{user_message}
"""

            result = mistral(prompt)
            return jsonify({"response": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

