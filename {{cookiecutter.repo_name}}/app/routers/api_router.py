from fastapi import APIRouter

from app.routers import user

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user.router)
