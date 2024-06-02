from fastapi import APIRouter

from app.routers import user
from app.settings import settings

api_router = APIRouter(prefix=settings.API_V1_STR)

api_router.include_router(user.router)
