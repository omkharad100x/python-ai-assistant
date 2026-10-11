
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check whether the API key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY was not found. Check your .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

print("AI Assistant is ready!")
print("Type 'exit' to quit.")

# Keep the assistant running
while True:
    question = input("\nYou: ")

    # Exit when the user types 'exit'
    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    # Handle errors during the API request
    try:
        print("Thinking...")

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        # Display Gemini's answer
        print("\nAssistant:", response.text)

    except Exception as error:
        print("\nAssistant: Sorry, something went wrong.")
        print("Error details:", error)
