
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

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
        max_retries = 3

        for attempt in range(max_retries):
            try:
                print("Thinking...")

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=question
                )

                print("\nAssistant:", response.text)
                break

            except errors.APIError as error:
                if error.code == 503 and attempt < max_retries - 1:
                    print("Gemini is busy. Retrying in 2 seconds...")
                    time.sleep(2)
                else:
                    raise


    
    except errors.APIError as error:
        print("\nAssistant: Gemini API request failed.")
        print("Error code:", error.code)
        print("Error details:", error.message)

    except Exception as error:
        print("\nAssistant: Something unexpected went wrong.")
        print("Error details:", error)

