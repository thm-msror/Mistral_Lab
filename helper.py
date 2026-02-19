from mistralai import Mistral, UserMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

def mistral(user_message, model="mistral-large-latest", is_json=False):
    client = Mistral(api_key=api_key)

    messages = [
        UserMessage(content=user_message),
    ]

    if is_json:
        chat_response = client.chat.complete(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        return chat_response.choices[0].message.content

    else:
        chat_response = client.chat.complete(
            model=model,
            messages=messages,
        )
        return chat_response.choices[0].message.content
