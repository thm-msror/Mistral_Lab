import streamlit as st
import requests

st.title("Mistral Customer Support Chatbot")

task = st.selectbox(
    "Select task",
    ["response", "classification", "summarize", "extract"]
)

user_input = st.text_area("Type your message here:")

if st.button("Send"):

    if user_input.strip() == "":
        st.warning("Please type a message!")
    else:
        try:
            response = requests.post(
                "http://localhost:5000/chat",
                json={"message": user_input, "task": task}
            )

            if response.status_code == 200:
                st.markdown(f"**Chatbot ({task}):**")
                st.write(response.json()["response"])
            else:
                st.error("Server error:")
                st.write(response.text)

        except Exception as e:
            st.error(f"Connection Error: {str(e)}")