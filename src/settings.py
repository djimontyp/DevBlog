import os
from functools import lru_cache
from typing import Literal, get_args

from pydantic import HttpUrl, EmailStr, PostgresDsn, BaseSettings

State = Literal["development", "production"]
ENV_FILE = ".env"


class ContactInfo(BaseSettings):
    name: str | None = None
    url: HttpUrl | None = None
    email: EmailStr | None = None

    class Config:
        env_file = ENV_FILE
        env_prefix = "ADMIN_"


class BaseConfig(BaseSettings):
    """Global application settings"""

    app_url: HttpUrl
    app_name: str
    db_url: PostgresDsn | str = "sqlite:///database.db"
    debug: bool = False
    contact: ContactInfo = ContactInfo()


class DevConfig(BaseConfig):
    class Config:
        env_file = ENV_FILE
        env_prefix = "DEV_"


class ProdConfig(BaseConfig):
    class Config:
        env_file = ENV_FILE
        env_prefix = "PROD_"


@lru_cache()
def get_settings():
    if not (state := os.getenv("APP_STATE")):
        raise ValueError(
            f"Environment variable `APP_STATE` must be set. "
            f"One of {get_args(State)}"
        )
    if state == "development":
        return DevConfig()
    else:
        return ProdConfig()


config = get_settings()

if __name__ == '__main__':
    from devtools import debug
    debug(config)
