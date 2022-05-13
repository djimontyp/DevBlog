__all__ = ['Catalog']

from datetime import datetime
from typing import Any

from pydantic import BaseModel
from pydantic.utils import GetterDict


class CatalogGetter(GetterDict):
    def get(self, key: str, default: Any) -> Any:  # noqa
        #: element attributes
        if key in {'date', 'text'}:
            return self._obj.attrib.get(key, default)
        #: element children
        else:
            try:
                return self._obj.find(key).tag
            except (AttributeError, KeyError):
                return default


class Catalog(BaseModel):
    shop: str
    date: datetime
    text: str

    class Config:
        orm_mode = True
        getter_dict = CatalogGetter
