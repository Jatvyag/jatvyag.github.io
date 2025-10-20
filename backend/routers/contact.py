from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, EmailStr, Field
import smtplib
from email.mime.text import MIMEText
import requests
import user_agents
from config import settings

GMAIL_USER = settings.GMAIL_USER
GMAIL_PASS = settings.GMAIL_PASS
EMAIL_FROM = settings.EMAIL_FROM
EMAIL_TO = settings.EMAIL_TO
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
    "userMessageSubject": 100,
    "userMessageText": 1000,
}


class ContactForm(BaseModel):
    userName: str = Field(..., max_length=MAX_LENGTH["userName"])
    userEmail: EmailStr = Field(..., max_length=MAX_LENGTH["userEmail"])
    userMessageSubject: str = Field(..., max_length=MAX_LENGTH["userMessageSubject"])
    userMessageText: str = Field(..., max_length=MAX_LENGTH["userMessageText"])
    locale: str = "en"
    userAgent: str | None = None


@router.post("")
async def contact(form: ContactForm, request: Request):
    msg = statusMessages.get(form.locale, statusMessages["en"])

    ua = user_agents.parse(form.userAgent or "")
    user_info = {
        "browser": ua.browser.family,
        "os": ua.os.family,
        "device": ua.device.family or "desktop",
    }

    email_body = f"""
Name: {form.userName}
Email: {form.userEmail}
Message: {form.userMessageText}
Locale: {form.locale}

Browser: {user_info["browser"]}
OS: {user_info["os"]}
Device: {user_info["device"]}
"""

    msg_email = MIMEText(email_body)
    msg_email["Subject"] = f"Contact Form: {form.userMessageSubject}"
    msg_email["From"] = EMAIL_FROM
    msg_email["To"] = EMAIL_TO

    telegram_message = f"""
📩 New Contact Form Message!

👤 Name: {form.userName}
📧 Email: {form.userEmail}
📝 Subject: {form.userMessageSubject}
🌎 Locale: {form.locale}

💬 Message:
{form.userMessageText}

🌐 Browser: {user_info["browser"]}
💻 OS: {user_info["os"]}
📱 Device: {user_info["device"]}
"""

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.send_message(msg_email)

        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": telegram_message},
        )

        return {"success": True, "message": msg["successMessage"]}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=msg["failedMessage"])
