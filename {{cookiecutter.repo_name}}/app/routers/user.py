from app.db import get_session
from app.schemas.token import Token
from app.services.user import UserService
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/token", status_code=status.HTTP_200_OK)
async def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
) -> Token:
    return await UserService.login(form_data, session)


@router.get("/login")
async def login(current_user=Depends(UserService.get_current_user)):
    return current_user
