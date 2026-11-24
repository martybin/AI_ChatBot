from langchain_ollama import ChatOllama
from app.config import Config

def get_llm() -> ChatOllama:
    """Create and return a ChatOllama instance using configuration from Config."""
    llm = ChatOllama(
        model=Config.OLLAMA_MODEL,
        base_url=Config.OLLAMA_BASE_URL,
        temperature=Config.LLM_TEMPERATURE
    )
    return llm
