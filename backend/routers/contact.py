from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx
import asyncio
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
import user_agents
from config import settings
from config import logger
from i18n.messages import get_locale_message

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

router = APIRouter(prefix="/contact", tags=["Contact"])

MAX_LENGTH = {
    "userName": 50,
    "userEmail": 100,
    "userMessageText": 1000,
}

class ContactForm(BaseModel):
    """Contact form model"""
    userName: Optional[str] = Field(None, max_length=MAX_LENGTH["userName"])
    userEmail: Optional[EmailStr] = Field(None, max_length=MAX_LENGTH["userEmail"])
    userMessageText: str = Field(..., max_length=MAX_LENGTH["userMessageText"])
    locale: str = "en"

    @field_validator("userEmail", mode="before")
    def empty_string_to_none(cls, input_value):
        """Converts empty strings to None"""
        if input_value == "":
            return None
        return input_value
    
    @model_validator(mode="after")
    def set_defaults(cls, model):
        """Sets default values for the form"""
        locale = model.locale
        if not model.userName:
            model.userName = get_locale_message("emptyDefault", locale)
        if not model.userEmail:
            model.userEmail = get_locale_message("emptyDefault", locale)
        return model


class TelegramSendError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


async def send_telegram_message(token, chat_id, message, locale):
    """Sends a message to the Telegram chat"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            response = await client.post(url, json={"chat_id": chat_id, "text": message})
            response.raise_for_status()
            logger.info("Telegram message sent successfully")
        except httpx.TimeoutException as e:
            logger.error(
                "Timeout while connecting to Telegram",
                exc_info=True,
                extra={"error": str(e)}
            )
            raise TelegramSendError(get_locale_message("timeOutTelegram", locale))
        except httpx.HTTPStatusError as e:
            logger.error(
                "Telegram API returned error",
                exc_info=True,
                extra={"status_code": e.response.status_code, "response": e.response.text}
            )
            raise TelegramSendError(get_locale_message("failedTelegramApi", locale))
        except httpx.RequestError as e:
            logger.error(
                "Network error while connecting to Telegram",
                exc_info=True,
                extra={"error": str(e)}
            )
            raise TelegramSendError(get_locale_message("failedTelegram", locale))
        except Exception as e:
            logger.error("Unexpected error sending Telegram message", exc_info=True)
            raise TelegramSendError(get_locale_message("failedTelegram", locale))


@router.post("")
async def contact(form: ContactForm, request: Request):
    """Contact form endpoint"""
    logger.info(f"Contact form received")

    user_agent_str = request.headers.get("user-agent", "")
    ua = user_agents.parse(user_agent_str)
    user_info = {
        "browser": ua.browser.family,
        "os": ua.os.family,
        "device": ua.device.family or "desktop",
    }

    telegram_message = f"""
📩 {get_locale_message("formTitle", form.locale)}!

👤 {get_locale_message("name", form.locale)}: {form.userName}
📧 {get_locale_message("email", form.locale)}: {form.userEmail}
🌎 {get_locale_message("locale", form.locale)}: {form.locale}

💬 {get_locale_message("message", form.locale)}:
{form.userMessageText}

🌐 {get_locale_message("browser", form.locale)}: {user_info["browser"]}
💻 {get_locale_message("os", form.locale)}: {user_info["os"]}
📱 {get_locale_message("device", form.locale)}: {user_info["device"]}
"""

    try:
        await asyncio.sleep(10)
        await send_telegram_message(
            TELEGRAM_TOKEN, 
            TELEGRAM_CHAT_ID, 
            telegram_message, 
            form.locale
        )
        return {"success": True, "message": get_locale_message("successMessage", form.locale)}
    except TelegramSendError as e:
        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "message": e.message
            }
        )
    except Exception as e:
        logger.error("Unexpected error", exc_info=True, extra={"error": str(e)})
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": get_locale_message("failedMessage", form.locale)
            }
        )
