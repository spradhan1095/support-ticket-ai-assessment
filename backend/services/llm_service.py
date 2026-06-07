from groq import Groq
from config import GROQ_API_KEY


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def identify_intent(self, question):

        prompt = f"""
You are an intent classifier.

Question:
{question}

Return ONLY one of these intents:

open_tickets
resolved_tickets
escalated_tickets
critical_tickets
unresolved_critical
average_rating
highest_rated_agent
lowest_rated_agent
most_common_category
average_response_time
average_resolution_time
unknown
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response
            .choices[0]
            .message
            .content
            .strip()
            .lower()
        )


llm_service = LLMService()