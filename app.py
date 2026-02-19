import streamlit as st
import requests

st.title("Mistral Customer Support Chatbot")

# ---------- Set API URL ----------
API_URL = st.secrets.get("API_URL")

if not API_URL:
    st.error("API_URL is not set. Please configure environment variable.")
    st.stop()

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
