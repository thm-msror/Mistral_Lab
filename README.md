# **Mistral Customer Support Chatbot**

A demo chatbot that can respond, classify, summarize, extract structured data, and provide personalized answers for customer support queries.

It consists of two main components:

1. **Flask API (`api.py`)** – handles the chatbot logic and communicates with the Mistral AI backend.
2. **Streamlit Frontend (`app.py`)** – a user-friendly interface to interact with the chatbot.

---

## **Live Demo Links**

| Component         | Link                                                                       | Description                                                                                                        |
| ----------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **API**           | _Private / internal_                                                       | The backend Flask API returns JSON responses for all tasks. Users normally interact through the frontend.          |
| **Streamlit App** | [https://mistral-lab-1.onrender.com/](https://mistral-lab-1.onrender.com/) | The user interface. Sends messages to the backend API and displays responses, including JSON for extraction tasks. |

> ⚠️ Note: The backend API may occasionally be unavailable if the server is down. If you see an error when sending messages, please wait a few minutes and try again.

---

## **Tasks Supported**

- **response** – General conversational response.
- **classification** – Categorize customer queries.
- **summarize** – Summarize long text.
- **extract** – Extract structured data in JSON (age, gender, diagnosis, weight, smoking).
- **personalized** – Address users by name in the response.

---

## **How It Works**

1. User enters a message in the Streamlit frontend.
2. Streamlit sends a POST request to the Flask backend API.
3. Flask selects the appropriate prompt for the task.
4. Flask sends the prompt to the Mistral AI model.
5. Mistral generates a response.
6. Flask returns JSON.
7. Streamlit displays the result in the UI.

**System Architecture:**

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

---

## **Project Structure**

```
Mistral_Lab/
│
├── api.py          # Flask backend
├── app.py          # Streamlit frontend
├── helper.py       # Mistral API logic
├── .env.example    # Example environment variables
├── requirements.txt
└── README.md
```

> **Note:** Do **not** commit your `.env` with real API keys. Use `.env.example` as a template.

---

## **.env.example**

```toml
# Copy this file to .env and fill in your credentials
MISTRAL_API_KEY=your_api_key_here
API_URL=http://127.0.0.1:5000/chat
```

> **Important:** The `API_URL` should point to your locally running backend (`http://127.0.0.1:5000/chat`) for local testing.

---

## **Setup Instructions (Local Testing)**

1. Clone the repo.
2. Copy `.env.example` to `.env`:

```bash
cp .env.example .env   # Linux / Mac
copy .env.example .env # Windows
```

3. Add your Mistral API key in `.env`.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. **Run the Flask backend** (required for frontend to work locally):

```bash
python api.py
```

> ⚠️ **Important:** If you don’t start the backend locally, the Streamlit frontend will **not work**, because it depends on the API to generate responses.

6. **Run the Streamlit frontend**:

```bash
streamlit run app.py
```

7. Open [http://localhost:8501](http://localhost:8501) to use the chatbot.

---

## **Online Usage**

- The frontend app hosted at Render connects to the backend API.
- If the Render backend goes down, the app will show an error:

```
"The backend API is currently unavailable. Please try again in a few minutes."
```

---

## **Chatbot Features**

- **Classification** – Categorizes customer queries (e.g., card arrival, change pin, exchange rate, cancel transfer).
- **Personalized Responses** – Generates responses addressing users by name.
- **Summarization** – Summarizes long messages into concise text.
- **Information Extraction** – Extracts structured JSON data from text.

---

## **Important Notes**

- Local backend port: **5000**
- Frontend port: **8501**
- Never commit your API keys or secrets to GitHub.
- If the backend is down (locally or online), the frontend cannot process messages.

---

## **Optional Improvements**

- Add chat memory to maintain conversation context.
- Create chat-style UI bubbles in Streamlit.
- Combine classification + automated responses.
- Deploy backend and frontend on a cloud platform (Render, Railway, or Streamlit Cloud).

---
