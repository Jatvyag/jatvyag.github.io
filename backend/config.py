from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GMAIL_USER = os.getenv("GMAIL_USER")
    GMAIL_PASS = os.getenv("GMAIL_PASS")
    EMAIL_FROM = os.getenv("EMAIL_FROM", GMAIL_USER)
    EMAIL_TO = os.getenv("EMAIL_TO")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

settings = Settings()
