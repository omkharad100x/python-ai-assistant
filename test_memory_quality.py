
# Example summary for a local memory-quality test
summary = """
- Favorite programming language: Python.
- Active project: Building a Python-based AI assistant.
- Model used: Gemini 3.1 Flash-Lite.
"""

# Important facts that should be preserved
required_facts = [
    "Python",
    "AI assistant",
    "Gemini 3.1 Flash-Lite",
]

missing_facts = [
    fact for fact in required_facts
    if fact.lower() not in summary.lower()
]

if missing_facts:
    print("Memory quality test failed.")
    print("Missing facts:", missing_facts)
else:
    print("Memory quality test passed.")
    print("All required facts are present.")
