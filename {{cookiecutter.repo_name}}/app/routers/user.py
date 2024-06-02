from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.db import SessionDep
from app.schemas.token import Token
from app.schemas.user import ChangePasswordIn, UserIn, UserOut
from app.services.user import CurrentUserDep, UserService

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserIn,
    session: SessionDep,
):
    return await UserService.register_user(user_data, session)


@router.post("/token", status_code=status.HTTP_200_OK)
async def token(
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    return await UserService.login(form_data, session)


@router.get("/login", status_code=status.HTTP_200_OK)
async def login(current_user: CurrentUserDep) -> UserOut:
    return UserOut.model_validate(current_user)


@router.get("/get_by_id/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: int,
    session: SessionDep,
) -> UserOut:
    return await UserService.get_user_by_id(user_id, session)


@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_all_users(session: SessionDep) -> list[UserOut]:
    return await UserService.get_all_users(session)


@router.delete("/delete_by_id/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user_by_id(
    user_id: int,
    session: SessionDep,
):
    return await UserService.delete_user_by_id(user_id, session)


@router.delete("/delete_all", status_code=status.HTTP_200_OK)
async def delete_all_users(session: SessionDep):
    return await UserService.delete_all_users(session)


@router.patch(
    "/change_password",
    status_code=status.HTTP_200_OK,
    summary="Change password for current user that is logged in",
)
async def change_password(
    session: SessionDep,
    password_data: ChangePasswordIn,
    current_user: CurrentUserDep,
):
    return await UserService.change_password(password_data, current_user, session)
