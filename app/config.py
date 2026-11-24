import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL", "http://localhost:11434"
        )
    
    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL", "mimo-v2.6:9b"
        )
    
    LLM_TEMPERATURE = float(
        os.getenv("LLM_TEMPERATURE", 0.3)
    )
