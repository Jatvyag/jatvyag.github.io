from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from i18n.messages import get_locale_message
import logging

logger = logging.getLogger(__name__)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Localized handler for validation errors"""
    try:
        body = await request.json()
        locale = body.get("locale", "en")
    except Exception:
        locale = "en"

    errors = []

    for err in exc.errors():
        field = err["loc"][-1]
        message = err["msg"]

        if "email" in message.lower():
            message = get_locale_message("invalidEmail", locale)
        elif "field required" in message.lower():
            message = get_locale_message("requiredField", locale)
        elif "at most" in message.lower() or "too long" in message.lower():
            max_len = err.get("ctx", {}).get("max_length")
            message = f"{get_locale_message('exceededChars', locale)}: {max_len}"

        errors.append({field: message})

    logger.warning("Validation failed", extra={"errors": errors, "locale": locale})

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": get_locale_message("failedValidation", locale),
            "errors": errors,
        },
    )


def register_error_handlers(app):
    """Attach custom error handlers to the FastAPI app"""
    from fastapi.exceptions import RequestValidationError
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
