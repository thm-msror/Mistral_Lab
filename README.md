# Mistral Customer Support Chatbot

This lab project demonstrates how to build and deploy a Customer Support Chatbot using Mistral AI.

The chatbot performs the following NLP tasks:

- Classification of customer inquiries
- Information extraction (JSON structured output)
- Summarization of text
- Personalized response generation

The system uses:

- Flask (Backend API)
- Streamlit (Frontend Web Interface)
- Mistral AI (Large Language Model)

---

# System Architecture

```
User (Streamlit UI)
↓
HTTP POST Request
↓
Flask API (/chat endpoint)
↓
Mistral LLM
↓
JSON Response
↓
Displayed in Streamlit
```

# Project Structure

```
Streamlit_Lab/
│
├── api.py # Flask backend
├── app.py # Streamlit frontend
├── helper.py # Mistral API logic
├── .env # API key (not pushed to GitHub)
├── requirements.txt
└── README.md
```

# Setup Instructions

## 1. Install Dependencies

Inside your project folder:

pip install -r requirements.txt

## 2. Add Your Mistral API Key

Create a `.env` file:

MISTRAL_API_KEY=your_api_key_here

## 3. Run the Flask Backend

Open Terminal 1:

```

python api.py

```

You should see:

```

Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

```

⚠️ Do NOT open port 5000 in the browser.
This is an API endpoint.

---

## 4. Run the Streamlit Frontend

Open Terminal 2:

```

streamlit run app.py

```

Open in browser:

```

[http://localhost:8501](http://localhost:8501)

```

This is your chatbot interface.

---

# Chatbot Features

The dropdown menu includes:

### 1️⃣ Classification

Classifies bank customer queries into:

- card arrival
- change pin
- exchange rate
- country support
- cancel transfer
- charge dispute
- customer service

### 2️⃣ Personalized Response

Generates a professional response to a customer inquiry.

### 3️⃣ Summarization

Summarizes long text into a concise summary.

### 4️⃣ Information Extraction

Extracts structured data (JSON format) from medical notes.

# How Flask Works

Flask acts as the backend server.

It:

- Receives user message from Streamlit
- Builds the appropriate prompt
- Sends request to Mistral
- Returns the generated response as JSON

Flask exposes an endpoint:

POST /chat

Example JSON request:

{
"message": "I lost my card",
"task": "classification"
}

# How Streamlit Works

Streamlit:

- Provides a user-friendly interface
- Sends HTTP requests to Flask
- Displays chatbot responses in real-time

# Important Notes

- Port 5000 → Flask API (backend)
- Port 8501 → Streamlit UI (chatbot)
- 404 on port 5000 is NORMAL
- Always open port 8501 to use the chatbot

# Optional Improvements

- Add chat memory
- Add chat-style UI bubbles
- Add automatic classification + response
- Deploy to Render / Railway / Streamlit Cloud
