## **Mistral Customer Support Chatbot**

A demo chatbot that can respond, classify, summarize, extract structured data, and provide personalized answers for customer support queries.

It consists of two main components:

1. **Flask API (`api.py`)** – handles the chatbot logic and communicates with the Mistral AI backend.
2. **Streamlit Frontend (`app.py`)** – a user-friendly interface to interact with the chatbot.

## **Live Demo Links**

| Component         | Link                                                                           | Description                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **API**           | [https://mistral-api.onrender.com](https://mistral-api.onrender.com)           | The backend Flask API. Returns JSON responses for all tasks.                                                                 |
| **Streamlit App** | [https://mistral-lab-3jmk.onrender.com](https://mistral-lab-3jmk.onrender.com) | The user interface. Interacts with the API to send messages and display results, including pretty JSON for extraction tasks. |

> Note: The frontend automatically calls the API, so you can interact with the chatbot directly from the Streamlit page.

## **Tasks Supported**

- **response** – General conversational response.
- **classification** – Categorize customer queries.
- **summarize** – Summarize long text.
- **extract** – Extract structured data in JSON (age, gender, diagnosis, weight, smoking).
- **personalized** – Address users by name in the response.

## **How It’s Deployed**

1. **Backend (Flask API)** – Deployed on **Render**:
   - The `api.py` file is served using **Gunicorn**.
   - URL: `https://mistral-api.onrender.com`
   - Handles POST requests at `/chat`.
   - Returns JSON responses depending on the selected task.

2. **Frontend (Streamlit App)** – Also deployed on **Render**:
   - The `app.py` file runs the Streamlit interface.
   - URL: `https://mistral-lab-3jmk.onrender.com`
   - Sends user messages to the backend API.
   - Displays results directly in the UI.

3. **Interaction Flow**:
   - User types a message in the Streamlit app → App sends request to Flask API → API processes with Mistral AI → Returns JSON → Streamlit displays response.

## **Usage**

1. Open the [Streamlit App](https://mistral-lab-3jmk.onrender.com).
2. Select a task from the dropdown.
3. Type your message in the text area.
4. If task is **personalized**, enter your name.
5. Click **Send**.
6. Results will display below the input:
   - **Extract** task shows structured JSON.
   - Other tasks show chatbot responses.

## Overview

This project implements a Customer Support Chatbot using:

- **Flask** → Backend API
- **Streamlit** → Frontend Web Interface
- **Mistral AI** → Large Language Model for NLP tasks

---

## What is Flask?

Flask is a lightweight Python web framework used to build APIs.

In this project:

- Flask acts as the backend server
- It receives user messages from Streamlit
- It sends prompts to Mistral AI
- It returns the AI-generated response as JSON

Flask handles the logic, while Streamlit handles the interface.

---

## What is Streamlit?

Streamlit is a Python framework for building interactive web apps.

In this project:

- It provides the chatbot interface
- Users type messages
- It sends HTTP requests to the Flask API
- It displays responses in the browser

---

## Chatbot Functionalities

The chatbot supports:

1. Classification
   Categorizes customer inquiries into predefined banking categories.

2. Information Extraction
   Extracts structured data from medical notes in JSON format.

3. Summarization
   Generates concise summaries of long text.

4. Personalized Responses
   Generates responses addressing customers by name with professional tone.

5. General Customer Support
   Provides professional responses to general queries.

---

## How It Works

1. User enters message in Streamlit.
2. Streamlit sends a POST request to Flask.
3. Flask selects the correct prompt.
4. Flask sends the prompt to Mistral AI.
5. Mistral generates a response.
6. Flask returns JSON.
7. Streamlit displays the result.

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
