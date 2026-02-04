AI Honeypot Middleware (Groq Edition)

- No Redis
- In-memory sessions
- Groq LLM (OpenAI-compatible)
- Human-like fallback mode

RUN:
python -m venv venv  
venv\Scripts\activate
pip install -r requirements.txt
export GROQ_API_KEY="<your_groq_key>"
export APP_API_KEY="<your_app_key>"
uvicorn app.main:app --reload
# HoneyPot
