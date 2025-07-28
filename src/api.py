from fastapi import FastAPI
from src.services.bookings.controller import router as bookings_router
from src.services.auth.controller import router as auth_router
from src.services.users.controller import router as users_router

def register_routes(app: FastAPI):
    app.include_router(bookings_router)
    app.include_router(auth_router)
    app.include_router(users_router)