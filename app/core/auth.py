from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from app.core.config import APP_API_KEY

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    # Accept either the configured APP_API_KEY or the hackathon default key
    valid_keys = ["scam-honeypot-hackathon-2026"]
    if APP_API_KEY:
        valid_keys.append(APP_API_KEY)
    
    if api_key in valid_keys:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials"
    )
