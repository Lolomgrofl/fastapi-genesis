from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, intpk, str100


class User(Base):
    __tablename__ = "user"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password: Mapped[str]
    first_name: Mapped[str100 | None]
    last_name: Mapped[str100 | None]
