from datetime import datetime
from typing import List

from pydantic import HttpUrl, Json, PositiveInt
from sqlmodel import SQLModel, Field

from constants import COUNTRIES_CODES


class CountryCode(SQLModel, table=True):
    id: PositiveInt | None = Field(default=None, primary_key=True)
    code: str


class Album(SQLModel):
    pass


class Artist(SQLModel):
    pass


class ExternalIds:
    spotify: HttpUrl


class TrackInfo(SQLModel):
    id: PositiveInt | None = Field(default=None, primary_key=True)

    album: Album | None = None
    artists: List[Artist] | None = []
    available_markets: List[str]
    disc_number: int | None = None
    duration_ms: int | None = None
    explicit: bool
    external_ids: Json
    external_urls: Json
    href: HttpUrl
    spotify_id: str = Field(alias="id")
    is_local: bool
    name: str
    popularity: int
    preview_url: HttpUrl | None = None
    track_number: int | None = None
    type: str
    uri: str


class Track(SQLModel):
    track: TrackInfo
    added_at: datetime


class Items(SQLModel):
    href: HttpUrl
    items: List[Track] = []
    limit: int
    next: HttpUrl | None = None
    offset: int
    previous: HttpUrl | None = None
    total: int
