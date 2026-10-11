
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from google.genai import types

# Load environment variables from .env
load_dotenv()

# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. Check your .env file."
    )

# Create the Gemini client
client = genai.Client(api_key=api_key)

print("AI Assistant is ready!")
print("Type 'exit' to quit.")
print("Type 'clear' to clear conversation history.")

# Store the conversation history
conversation_history = []

MAX_HISTORY_MESSAGES = 20

# Keep the assistant running
while True:
    question = input("\nYou: ").strip()

    # Handle empty questions
    if not question:
        print("Assistant: Please enter a question.")
        continue

    # Exit the assistant
    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    # Clear conversation history
    if question.lower() == "clear":
        conversation_history.clear()
        print("Assistant: Conversation history cleared.")
        continue

    # Retry temporary API errors
    max_retries = 3

    for attempt in range(max_retries):
        try:
            print("Thinking...")

            # Add the new user message to the history
            conversation_history.append(
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=question)]
                )
            )

            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=conversation_history
            )

            # Display and store the assistant's answer
            if response.text:
                print("\nAssistant:", response.text)

                conversation_history.append(
                    types.Content(
                        role="model",
                        parts=[
                            types.Part.from_text(text=response.text)
                        ]
                    )
                )

                
                # Keep the most recent messages in complete pairs
                if len(conversation_history) > MAX_HISTORY_MESSAGES:
                    conversation_history = conversation_history[-MAX_HISTORY_MESSAGES:]

                    # Remove a leading assistant response if its question was trimmed
                    if conversation_history[0].role == "model":
                        conversation_history.pop(0)



            else:
                print("\nAssistant: I received an empty response.")
                conversation_history.pop()

            # Stop retrying after success
            break

        except errors.APIError as error:
            # Remove the failed user message before retrying
            if (
                conversation_history
                and getattr(conversation_history[-1], "role", None) == "user"
            ):
                conversation_history.pop()

            # Retry temporary server errors
            if error.code == 503 and attempt < max_retries - 1:
                print("Gemini is busy. Retrying in 2 seconds...")
                time.sleep(2)
            
            else:
                error_message = str(error.message).lower()

                if (
                    "quota" in error_message
                    or "rate limit" in error_message
                    or "resource_exhausted" in error_message
                ):
                    print(
                        "\nAssistant: You've reached the Gemini API usage limit."
                    )
                    print(
                        "Please wait for your quota to reset before trying again."
                    )
                else:
                    print("\nAssistant: Gemini API request failed.")
                    print("Error code:", error.code)
                    print("Error details:", error.message)

            break


        except Exception as error:
            # Remove the user message if the request fails
            if (
                conversation_history
                and getattr(conversation_history[-1], "role", None) == "user"
            ):
                conversation_history.pop()

            print("\nAssistant: Something unexpected went wrong.")
            print("Error details:", error)
            break
