
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")

client = genai.Client(api_key=api_key)

# A small sample conversation for testing
sample_messages = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(
            text="My favorite programming language is Python."
        )]
    ),
    types.Content(
        role="model",
        parts=[types.Part.from_text(
            text="Got it. Your favorite programming language is Python."
        )]
    ),
    types.Content(
        role="user",
        parts=[types.Part.from_text(
            text="I am building a Python AI assistant."
        )]
    ),
    types.Content(
        role="model",
        parts=[types.Part.from_text(
            text="That sounds like a useful project."
        )]
    ),
]

prompt = """
Create a concise long-term memory from this conversation.

Preserve useful facts and project details.
Do not invent information.
Return only the memory summary.

Existing memory:
No memories saved yet.

Conversation:
"""

for message in sample_messages:
    role = "Assistant" if message.role == "model" else "User"
    prompt += f"\n{role}: {message.parts[0].text}"

print("Testing memory summarization...")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

if response.text:
    updated_memory = response.text.strip()

    with open("test_memory_output.txt", "w", encoding="utf-8") as file:
        file.write(updated_memory)

    print("\nGenerated summary:")
    print(updated_memory)
    print("\nTest summary saved to test_memory_output.txt.")
else:
    print("Gemini returned an empty response.")
