import os
from groq import Groq

class GroqLLM:
    def __init__(self, model_name=None, api_key=None):
        self.model_name = model_name or os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)

    def call(self, prompt, temperature=0.2, max_tokens=1024):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
