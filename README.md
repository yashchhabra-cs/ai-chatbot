# AI Chatbot Web App

A full-stack conversational AI chatbot built with the Claude API, Flask, and JavaScript.

## Features
- Real-time token streaming via Claude API
- Python Flask backend with prompt engineering
- Responsive frontend with dynamic message rendering
- Production-grade error handling and rate-limit management

## Tech Stack
- **Backend:** Python, Flask, Claude API (Anthropic)
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Tools:** Git, VS Code, Claude Code

## Setup

1. Clone the repo
```bash
git clone https://github.com/yashchhabra-cs/ai-chatbot.git
cd ai-chatbot
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Add your API key
```bash
cp .env.example .env
# Add your Anthropic API key to .env
```

4. Run the app
```bash
python app.py
```

## Author
Yash Chhabra — [LinkedIn](https://linkedin.com/in/yash-chhabra-07cs) | [GitHub](https://github.com/yashchhabra-cs)
