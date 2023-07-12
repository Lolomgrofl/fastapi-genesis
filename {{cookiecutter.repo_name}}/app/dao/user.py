from app.dao.base import BaseDao
from app.models.user import User
from sqlalchemy import delete, select
from sqlalchemy.orm import Session


class UserDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    async def create(self, request) -> User:
        _user = User(request)
        self.session.add(_user)
        self.session.commit()
        self.session.refresh(_user)
        return _user

    async def get_by_id(self, user_id: int) -> User:
        statement = select(User).where(User.id == user_id)
        return self.session.scalar(statement=statement)

    async def get_by_email(self, email) -> User:
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement=statement)

    async def get_all(self) -> list[User]:
        statement = select(User).order_by(User.id)
        return self.session.scalars(statement=statement).all()

    async def delete_all(self) -> None:
        self.session.execute(delete(User))
