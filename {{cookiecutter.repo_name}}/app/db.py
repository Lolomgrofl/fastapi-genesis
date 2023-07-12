from app.config import settings
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

postgres_url = settings.SQLALCHEMY_URL

engine = create_engine(postgres_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as err:
        logger.exception(f"Something broke... Rollback!!! Error:{err}", exc_info=err)
        session.rollback()
    finally:
        session.close()
        logger.info("Connection closed!")
