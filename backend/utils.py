from faker import Faker

from config import Settings, get_settings

fake = Faker()


def image_url(filename: str, s: Settings = get_settings()) -> str:
    # TODO fix pretty build URL
    return f"{s.APP_URL}/static/images/books/{filename}"
