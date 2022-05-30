from functools import lru_cache

from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    DB_URL: str = "sqlite:///database.db"
    APP_URL: HttpUrl
    APP_NAME: str
    ADMIN_EMAIL: str
    DEBUG: bool = False

    class Config:
        env_file = "development.env"


@lru_cache()
def get_settings():
    return Settings()


dev_settings = get_settings()
