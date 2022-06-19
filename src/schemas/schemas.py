from typing import List

from pydantic import BaseModel, conint, validator

from utils import image_url


class Book(BaseModel):
    title: str
    image: str
    pages: conint(gt=0)  # pages > 0
    page: conint(ge=0)  # page >= 0

    @validator('image')
    def image_url_builder(cls, filename):
        return image_url(filename)

    @classmethod
    def all(cls) -> List["Book"]:
        return [
            cls(
                title="Чистый Python. Тонкости программирования для профи.",
                image="CleanPython.jpg",
                pages=288,
                page=288
            ),
            cls(
                title="Python. Разработка на основе тестирования.",
                image="TDD.jpg",
                pages=624,
                page=77,
            ),
        ]


class Item(BaseModel):
    title: str
    image: str
    price: conint(gt=0)  # price > 0
    article: str

    @classmethod
    def get(cls) -> "Item":
        return cls(
            image="https://atlantmarket.com.ua/upload/iblock/7d4/13479.JPG.jpg",
            title="Ніж складний Ganzo G7361-WD1 дерево",
            price=1000,
            article="G7361-WD1"
        )
