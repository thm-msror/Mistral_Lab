from flask import Flask, request, jsonify
from helper import mistral

app = Flask(__name__)

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

        if task == "classification":

            prompt = f"""
You are a bank customer service bot.

Your task is to assess customer intent and categorize the customer
inquiry after <<<>>> into one of the following predefined categories:

- card arrival
- change pin
- exchange rate
- country support
- cancel transfer
- charge dispute

If the text doesn't fit into any of the above categories,
classify it as:
- customer service

You will only respond with the predefined category.
Do not provide explanations or notes.

<<<
Inquiry: {user_message}
>>>
Category:
"""

        elif task == "extract":

            prompt = f"""
Extract information from the following medical notes:
{user_message}

Return json format with the following JSON schema:
{{"age": {{"type": "integer"}},
"gender": {{"type": "string","enum": ["male", "female", "other"]}},
"diagnosis": {{"type": "string","enum": ["migraine", "diabetes", "arthritis", "acne"]}},
"weight": {{"type": "integer"}},
"smoking": {{"type": "string","enum": ["yes", "no"]}}}}
"""

        elif task == "summarize":

            prompt = f"""
Summarize the following text clearly and concisely:

{user_message}
"""

        elif task == "personalized":

            prompt = f"""
You are a professional bank customer support assistant.

Address the customer by their name: {user_name}

Respond to their inquiry clearly, professionally, and in a friendly tone.
Provide helpful information and close politely.

Customer Inquiry:
{user_message}

Sign the message as:
Bank Customer Support
"""

        else:  # response

            prompt = f"""
You are a helpful customer service assistant.
Respond professionally and clearly to the customer:

{user_message}
"""

        result = mistral(prompt)

        return jsonify({"response": result})

    except Exception as e:
        return jsonify({"response": f"Server Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
