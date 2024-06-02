from fastapi import Depends

from collections.abc import AsyncGenerator
from typing import Annotated

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.settings import settings

postgres_url = settings.POSTGRES_URL.unicode_string()

engine = create_async_engine(postgres_url, echo=True, future=True)
AsyncSessionFactory = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
