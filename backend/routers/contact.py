from fastapi import APIRouter, HTTPException, Request
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator
import requests
import user_agents
from config import settings

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

router = APIRouter(prefix="/contact", tags=["Contact"])

statusMessages = {
    "en": {
        "requiredField": "Missing required fields",
        "invalidEmail": "Invalid email address",
        "exscidedChars": "Exceeded character limit: ",
        "successMessage": "Message received!",
        "failedMessage": "Failed to send message",
    },
    "be": {
        "requiredField": "Адсутнічаюць абавязковыя палі",
        "invalidEmail": "Няправільны адрас электроннай пошты",
        "exscidedChars": "Перавышана максімальная даўжыня сымбалі: ",
        "successMessage": "Паведамленне атрымана!",
        "failedMessage": "Не атрымалася адправіць паведамленне",
    },
}

MAX_LENGTH = {
    "userName": 50,
    "userEmail": 100,
    "userMessageText": 1000,
}


class ContactForm(BaseModel):
    userName: str = Field(..., max_length=MAX_LENGTH["userName"])
    userEmail: Optional[EmailStr] = Field(None, max_length=MAX_LENGTH["userEmail"])
    userMessageText: str = Field(..., max_length=MAX_LENGTH["userMessageText"])
    locale: str = "en"
    userAgent: str | None = None

    @validator("userEmail", pre=True)
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v


@router.post("")
async def contact(form: ContactForm, request: Request):
    msg = statusMessages.get(form.locale, statusMessages["en"])

    ua = user_agents.parse(form.userAgent or "")
    user_info = {
        "browser": ua.browser.family,
        "os": ua.os.family,
        "device": ua.device.family or "desktop",
    }

    telegram_message = f"""
📩 New Contact Form Message!

👤 Name: {form.userName}
📧 Email: {form.userEmail}
🌎 Locale: {form.locale}

💬 Message:
{form.userMessageText}

🌐 Browser: {user_info["browser"]}
💻 OS: {user_info["os"]}
📱 Device: {user_info["device"]}
"""

    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": telegram_message},
        )
        return {"success": True, "message": msg["successMessage"]}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=msg["failedMessage"])
