from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

CSV_PATH = os.getenv(
    "CSV_PATH",
    "backend/data/support_tickets.csv"
)