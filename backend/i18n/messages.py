form_labels = {
    "emptyDefault": {
        "en": "Not Specified",
        "be": "Не пазначана"
    },
    "formTitle": {
        "en": "New Contact Form Message",
        "be": "Новае паведамленне з кантактнай формы"
    },
    "name": {
        "en": "Name",
        "be": "Імя"
    },
    "email": {
        "en": "Email",
        "be": "Электронная пошта"
    },
    "locale": {
        "en": "Locale",
        "be": "Мова"
    },
    "message": {
        "en": "Message",
        "be": "Паведамленне"
    },
    "browser": {
        "en": "Browser",
        "be": "Браўзер"
    },
    "os": {
        "en": "OS",
        "be": "АС"
    },
    "device": {
        "en": "Device",
        "be": "Прылада"
    },
}

invalid_validation = {
    "invalidEmail": {
        "en": "Invalid email address",
        "be": "Неправільны адрас электроннай пошты"
    },
    "requiredField": {
        "en": "Missing required field",
        "be": "Поле абавязкова для запоўнення"
    },
    "exceededChars": {
        "en": "Exceeded character limit",
        "be": "Перавышаны ліміт сімвалаў"
    },
    "failedValidation": {
        "en": "Form is invalid",
        "be": "Форма не правільна запоўнена"
    },
}

status_form_messages = {
    "successMessage": {
        "en": "Message received!",
        "be": "Паведамленне атрымана!"
    },
    "failedMessage": {
        "en": "Failed to send message",
        "be": "Не атрымалася адправіць паведамленне"
    },
    "failedConnection": {
        "en": "Failed to connect to the server",
        "be": "Не атрымалася падключыцца да сервера"
    },
    "timeOutTelegram": {
        "en": "Timed out while sending message to Telegram",
        "be": "Час адпраўкі паведамлення ў Telegram выйшаў"
    },
    "failedTelegram": {
        "en": "Failed to send message to Telegram",
        "be": "Не атрымалася адправіць паведамленне ў Telegram"
    },
    "failedTelegramApi": {
        "en": "Telegram API returned error",
        "be": "Telegram API вярнуў памылку"
    },
}

def get_locale_message(key: str, locale: str = "en"):
    """Return localized string for a given key"""
    for source in [form_labels, invalid_validation, status_form_messages]:
        if key in source:
            return source[key].get(locale, source[key].get("en"))
    return key
