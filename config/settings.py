import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # AI Configuration
    AI_MODEL = "openai/gpt-4o-mini"
    BASE_URL = "https://openrouter.ai/api/v1"
    API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Framework Timeouts
    DEFAULT_TIMEOUT = 5000  # ms
    HEALING_ENABLED = True
    
    # Project Info (for OpenRouter headers)
    SITE_URL = "https://github.com/your-username/self-healing-playwright"
    APP_NAME = "Self-Healing QA Framework"