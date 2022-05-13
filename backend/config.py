from functools import lru_cache

from pydantic import BaseSettings, HttpUrl
from sqlmodel import create_engine


class Settings(BaseSettings):
    DB_URL: str = "sqlite:///database.db"
    APP_NAME: str
    APP_URL: HttpUrl
    ADMIN_EMAIL: str
    DEBUG: bool

    class Config:
        env_file = "development.env"


@lru_cache()
def get_settings():
    return Settings()
