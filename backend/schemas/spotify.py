from datetime import datetime
from typing import List, Dict, Optional

from pydantic import BaseModel, HttpUrl


class Track(BaseModel):
    album: Optional[Dict] = None
    artists: Optional[List] = None
    available_markets: List[str]
    disc_number: Optional[int] = None
    duration_ms: Optional[int] = None
    explicit: bool
    external_ids: Optional[Dict] = None
    external_urls: Optional[Dict] = None
    href: Optional[HttpUrl] = None
    id: Optional[str] = None
    is_local: bool
    name: Optional[str] = None
    popularity: Optional[int] = None
    preview_url: Optional[HttpUrl] = None
    track_number: Optional[int] = None
    type: Optional[str] = None
    uri: Optional[str] = None


class UserTrack(BaseModel):
    added_at: datetime
    track: Track


class UserTracks(BaseModel):
    href: HttpUrl
    previous: Optional[HttpUrl] = None
    next: Optional[HttpUrl] = None
    items: List[UserTrack] = []
    limit: int
    offset: int
    total: int
