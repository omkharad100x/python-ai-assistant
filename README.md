# Python AI Assistant

A simple terminal-based AI assistant built with Python and Google's Gemini API.

This project was created to learn how to connect Python applications to large language models (LLMs), handle API errors, and build reliable AI-powered applications.

## Features

- Interactive question-and-answer experience
- Powered by Gemini 3.8 Flash
- Secure API key loading from environment variables
- Empty-input validation
- Basic API error handling
- Automatic retries for temporary HTTP 503 errors
- Clean exit using the `exit` command

## Tech Stack

- Python
- Google Gen AI SDK (`google-genai`)
- `python-dotenv`
- Gemini API

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/omkharad100x/python-ai-assistant
cd python-ai-assistant
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure your API key

Create a file named `.env` in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own Gemini API key. Never commit or share your actual key.

### 5. Run the assistant

```powershell
python main.py
```

Type a question to receive an answer. Type `exit` to quit.

## Project Structure

```text
python-ai-assistant/
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
└── .env
```

The `.env` file is local and should be excluded from Git.

## Learning Goals

This project explores Python application structure, API integration, environment variables, error handling, retry logic, and Git/GitHub workflows.

## Future Improvements

- Conversation history and context
- Clear-conversation command
- Tool calling
- AI agent capabilities

## License

No license has been specified yet.