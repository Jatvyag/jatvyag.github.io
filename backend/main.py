from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contact, health
from errors.handlers import register_error_handlers

app = FastAPI(title="My FastAPI Backend")

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://jatvyag.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "Accept", "Origin"],
)

# Register error handlers
register_error_handlers(app)

# Register routers
app.include_router(health.router)
app.include_router(contact.router)

