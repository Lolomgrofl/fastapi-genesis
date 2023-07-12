from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str | None
    last_name: str | None

    class Config:
        orm_mode = True


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int
