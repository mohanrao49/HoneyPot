# ===== CONFIG =====
LLM_PROVIDER = "groq"   # groq | none
GROQ_API_KEY = __import__("os").getenv("GROQ_API_KEY", "")       # optional
GROQ_MODEL = "llama3-70b-8192"

SCAM_THRESHOLD = 0.15
MAX_TURNS = 8

# Authentication
APP_API_KEY = __import__("os").getenv("APP_API_KEY", "")
