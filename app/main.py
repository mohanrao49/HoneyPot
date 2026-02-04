from fastapi import FastAPI, Depends
from app.schemas.models import MessageInput, AIResponse
from app.router import process_message
from app.core.auth import get_api_key
from app.core.config import GROQ_API_KEY, LLM_PROVIDER, APP_API_KEY
import os

app = FastAPI(title="AI Honeypot", version="1.0.0")

@app.get("/")
def root():
    return {"status": "ok", "message": "AI Honeypot is running"}

@app.get("/health")
def health_check():
    groq_configured = bool(GROQ_API_KEY)
    app_auth_configured = bool(APP_API_KEY)
    
    return {
        "status": "healthy",
        "llm_provider": LLM_PROVIDER,
        "groq_configured": groq_configured,
        "auth_configured": app_auth_configured,
        "groq_key_length": len(GROQ_API_KEY) if groq_configured else 0,
        "environment": os.getenv("RENDER", "local")
    }

@app.post("/ai/message", response_model=AIResponse, dependencies=[Depends(get_api_key)])
def ai_message(input: MessageInput):
    return process_message(input)
