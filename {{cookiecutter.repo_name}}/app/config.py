from pydantic import BaseSettings


class Config(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    SQLALCHEMY_URL: str

    class Config:
        env_file = "./.env"


settings = Config()
