from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.schemas.token import Token
from app.schemas.user import UserIn, UserOut
from app.services.user import UserService

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserIn,
    session: AsyncSession = Depends(get_session),
):
    return await UserService.register_user(user_data, session)


@router.post("/token", status_code=status.HTTP_200_OK)
async def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
) -> Token:
    return await UserService.login(form_data, session)


@router.get("/login", status_code=status.HTTP_200_OK)
async def login(current_user=Depends(UserService.get_current_user)):
    return current_user


@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_all_users(session: AsyncSession = Depends(get_session)) -> list[UserOut]:
    return await UserService.get_all_users(session)


@router.delete("/delete_all", status_code=status.HTTP_200_OK)
async def delete_all_users(session: AsyncSession = Depends(get_session)):
    return await UserService.delete_all_users(session)
