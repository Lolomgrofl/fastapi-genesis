from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    SQLALCHEMY_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATE_FORMAT: str

    class Config:
        env_file = "./.env"


settings = Settings()
