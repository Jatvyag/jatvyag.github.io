from dotenv import load_dotenv
import os
import logging
import sys
import json

load_dotenv()

class Settings:
    ENV=os.getenv("ENV")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

settings = Settings()

ENV = settings.ENV

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "name": record.name,
            "time": self.formatTime(record),
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "line": record.lineno,
        }
        return json.dumps(log_record)

logger = logging.getLogger("contact_form")
if ENV == "DEV":
    logger.setLevel(logging.INFO)
elif ENV == "PROD":
    logger.setLevel(logging.WARNING)
elif ENV == "DEBUG":
    logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
