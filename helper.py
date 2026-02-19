import os
from dotenv import load_dotenv
from mistralai import Mistral, UserMessage

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

def mistral(user_message, model="mistral-large-latest"):
    try:
        client = Mistral(api_key=api_key)

        messages = [
            UserMessage(content=user_message),
        ]

        chat_response = client.chat.complete(
            model=model,
            messages=messages,
        )

        return chat_response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"
