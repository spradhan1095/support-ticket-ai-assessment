from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def ask(self, prompt):

        response = self.client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a support ticket analyst.

                    Return concise answers.

                    Use only the supplied context.
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content


llm_service = LLMService()