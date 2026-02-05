import os
import openai
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv()

class PlaywrightHealer:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(" OPENAI_API_KEY not found. Ensure .env is configured.")
        
        # Configure for OpenRouter
        self.client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
            default_headers={
                "X-Title": "Self-Healing-Playwright-Framework",
            }
        )

    def suggest_new_selector(self, broken_selector, page_source):
        """
        Requests a new CSS selector from the LLM based on DOM context.
        """
        # Prompt engineering: specifically asking for CSS selectors to maintain Playwright compatibility
        prompt = f"""
        Target element with selector '{broken_selector}' was not found.
        Analyze the HTML snippet below and find the most likely new CSS selector for this element.
        Return ONLY the CSS selector string, no prose or markdown.
        
        HTML Content:
        {page_source[:3000]}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="openai/gpt-4o-mini", # Optimized for speed/cost
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip().replace('`', '')
        except Exception as e:
            print(f" AI Healing API Error: {e}")
            return None