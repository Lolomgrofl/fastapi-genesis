from datetime import timedelta

from app.daos import user
from app.db import get_session
from app.schemas.token import Token, TokenData
from app.schemas.user import UserIn, UserOut
from app.services.utils import UtilsService, oauth2_scheme
from app.settings import settings
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from loguru import logger
from sqlalchemy.orm import Session


class UserService:
    @staticmethod
    async def register_user(user_data: UserIn, session: Session):
        user_exist = await UserService.user_email_exists(session, user_data.email)

        if user_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with the given email already exists!!!",
            )

        user_data.password = UtilsService.get_password_hash(user_data.password)
        new_user = await user.UserDao(session).create(user_data.model_dump())
        logger.info(f"New user created successfully: {new_user}!!!")
        return JSONResponse(
            content={"message": "User created successfully"},
            status_code=status.HTTP_201_CREATED,
        )

    @staticmethod
    async def authenticate_user(session: Session, email: str, password: str):
        _user = await user.UserDao(session).get_by_email(email)
        if not _user:
            return False
        if not UtilsService.verify_password(password, _user.password):
            return False
        return _user

    @staticmethod
    async def user_email_exists(session: Session, email):
        _user = await user.UserDao(session).get_by_email(email)
        return _user if _user else None

    @staticmethod
    async def login(form_data: OAuth2PasswordRequestForm, session: Session) -> Token:
        _user = await UserService.authenticate_user(
            session, form_data.username, form_data.password
        )
        if not _user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password",
            )

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = UtilsService.create_access_token(
            data={"sub": _user.email}, expires_delta=access_token_expires
        )
        token_data = {
            "access_token": access_token,
            "token_type": "Bearer",
        }
        return Token(**token_data)

    @staticmethod
    async def get_current_user(
        session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)
    ) -> UserOut:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            email: str = payload.get("sub")
            if not email:
                raise credentials_exception
            token_data = TokenData(email=email)
        except JWTError:
            raise credentials_exception
        _user = await user.UserDao(session).get_by_email(email=token_data.email)
        if not _user:
            raise credentials_exception
        return UserOut.model_validate(_user)

    @staticmethod
    async def get_all_users(session: Session):
        all_users = await user.UserDao(session).get_all()
        return [UserOut.model_validate(_user) for _user in all_users]

    @staticmethod
    async def delete_all_users(session: Session):
        await user.UserDao(session).delete_all()
        return JSONResponse(
            content={"message": "All users deleted successfully!!!"},
            status_code=status.HTTP_200_OK,
        )
