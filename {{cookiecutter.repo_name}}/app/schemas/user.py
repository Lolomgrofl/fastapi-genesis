from pydantic import ConfigDict, BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str | None
    last_name: str | None
    model_config = ConfigDict(from_attributes=True)


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int
