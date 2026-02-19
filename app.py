from dotenv import load_dotenv
import os
import streamlit as st
import requests

# Load .env file
load_dotenv()

st.title("Mistral Customer Support Chatbot")

# ---------- Set API URL ----------
API_URL = os.environ.get("API_URL")

# Helper function
def send_message(message, task="response", name="Customer"):
    payload = {
        "message": message,
        "task": task,
        "name": name
    }
    response = requests.post(API_URL, json=payload)
    return response.json()

# ---------- UI ----------
task = st.selectbox(
    "Select task",
    ["response", "classification", "summarize", "extract", "personalized"]
)

user_name = ""
if task == "personalized":
    user_name = st.text_input("Enter your name")

user_input = st.text_area("Type your message here:")

if st.button("Send"):

    if user_input:
        try:
            data = send_message(user_input, task, user_name)

            if task == "extract":
                st.json(data)
            else:
                st.markdown(f"**Chatbot ({task}):** {data['response']}")

        except Exception as e:
            st.error(f"Connection error: {e}")

    else:
        st.warning("Please type a message!")
