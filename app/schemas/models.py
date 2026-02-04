from pydantic import BaseModel, Field
from typing import Dict, Optional

class MessageInput(BaseModel):
    sessionId: Optional[str] = None
    message: str

    class Config:
        populate_by_name = True
        extra = "allow" # Be permissive

class AIResponse(BaseModel):
    sessionId: str
    reply: str
    extractedIntelligence: Dict

    class Config:
        populate_by_name = True
