from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_FLASH_2_API"))

history = []

user_input = input("Bot: Hi, How can I help you?\n")
history.append(user_input)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash", contents=history
)

while True:
    current_response = ""
    for chunk in response:
        print(chunk.text, end="")
        current_response += chunk.text

    history.append(current_response)

    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break
    history.append(user_input)

    response = client.models.generate_content_stream(
        model="gemini-2.0-flash", contents=history
    )
