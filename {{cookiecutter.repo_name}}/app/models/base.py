from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True, index=True, autoincrement=True)]
str100 = Annotated[str, 100]
