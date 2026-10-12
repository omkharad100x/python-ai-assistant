
from google.genai import types

# Create 12 sample exchanges (24 messages).
conversation_history = []

for number in range(1, 13):
    conversation_history.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=f"Question {number}")]
        )
    )

    conversation_history.append(
        types.Content(
            role="model",
            parts=[types.Part.from_text(text=f"Answer {number}")]
        )
    )

RECENT_EXCHANGES_TO_KEEP = 10
recent_message_count = RECENT_EXCHANGES_TO_KEEP * 2

older_messages = conversation_history[:-recent_message_count]
recent_messages = conversation_history[-recent_message_count:]

print("Total messages:", len(conversation_history))
print("Older messages:", len(older_messages))
print("Recent messages:", len(recent_messages))

print("\nFirst older message:", older_messages[0].parts[0].text)
print("Last older message:", older_messages[-1].parts[0].text)

print("\nFirst recent message:", recent_messages[0].parts[0].text)
print("Last recent message:", recent_messages[-1].parts[0].text)
