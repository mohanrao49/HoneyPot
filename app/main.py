from fastapi import FastAPI, Depends, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.schemas.models import MessageInput, AIResponse
from app.router import process_message
from app.core.auth import get_api_key
from app.core.config import GROQ_API_KEY, LLM_PROVIDER, APP_API_KEY
import os

app = FastAPI(title="AI Honeypot", version="1.0.0")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Log the raw body for debugging
    body = await request.body()
    print(f"Validation error. Raw body: {body.decode()}")
    print(f"Errors: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

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

@app.post("/analyze", response_model=AIResponse, dependencies=[Depends(get_api_key)])
async def analyze(request: Request):
    # Try to parse the body flexibly
    try:
        body = await request.json()
        print(f"Received body: {body}")
        
        # Accept both 'message' directly or nested structures
        message = body.get('message', '')
        session_id = body.get('sessionId') or body.get('session_id')
        
        if not message:
            return JSONResponse(
                status_code=400,
                content={"detail": "Missing 'message' field"}
            )
        
        # Create the input object
        input_obj = MessageInput(message=message, sessionId=session_id)
        return process_message(input_obj)
    except Exception as e:
        print(f"Error processing request: {e}")
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)}
        )
