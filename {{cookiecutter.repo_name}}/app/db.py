from app.settings import settings
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
        logger.exception("Something broke...Rollback!!!", exc_info=err)
        session.rollback()
    finally:
        session.close()
        logger.info("Connection closed!!!")
