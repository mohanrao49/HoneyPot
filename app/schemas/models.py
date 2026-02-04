from pydantic import BaseModel, Field
from typing import Dict, Optional

class MessageInput(BaseModel):
    sessionId: Optional[str] = Field(None, alias="session_id")
    message: str

    class Config:
        populate_by_name = True

class AIResponse(BaseModel):
    sessionId: str = Field(..., alias="session_id")
    reply: str
    extractedIntelligence: Dict = Field(..., alias="extracted_intelligence")

    class Config:
        populate_by_name = True
