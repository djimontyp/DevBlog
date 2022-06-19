from faker import Faker

from settings import BaseConfig, get_settings

fake = Faker()


def image_url(filename: str, s: BaseConfig = get_settings()) -> str:
    # TODO fix pretty build URL
    return f"{s.app_url}/static/images/books/{filename}"
