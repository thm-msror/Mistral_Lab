import streamlit as st
import requests

st.title("Mistral Customer Support Chatbot")

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

        payload = {
            "message": user_input,
            "task": task,
            "name": user_name
        }

        try:
            response = requests.post(
                "http://localhost:5000/chat",
                json=payload
            )

            if response.status_code == 200:
                data = response.json()

                if task == "extract":
                    st.json(data)   # Pretty JSON output
                else:
                    st.markdown(f"**Chatbot ({task}):** {data['response']}")

            else:
                st.error("Error communicating with API")

        except Exception as e:
            st.error(f"Connection error: {e}")

    else:
        st.warning("Please type a message!")
