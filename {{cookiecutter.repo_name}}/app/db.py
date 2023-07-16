from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

postgres_url = settings.POSTGRES_URL.unicode_string()

engine = create_async_engine(postgres_url, echo=True, future=True)
AsyncSessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session
