import xml.etree.ElementTree as ElementTree
from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlmodel import create_engine, SQLModel
from starlette.middleware.cors import CORSMiddleware

from config import get_settings
from schemas.atlantmarket import Catalog
from schemas.schemas import Book
from schemas.spotify import UserTracks
from spotify import client

origins = ['*']

settings = get_settings()

engine = create_engine(settings.DB_URL, echo=True)

SQLModel.metadata.create_all(engine)

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    contact={"email": settings.ADMIN_EMAIL}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', name='homepage', include_in_schema=False)
async def homepage():
    return RedirectResponse('/docs')


@app.get('/books', response_model=List[Book], name='books')
async def books():
    return Book.all()


@app.get('/catalogs/{id}', response_model=Catalog, name='parsers')
async def item(id: str) -> Catalog:
    datas = Path('test_data')
    file = datas.joinpath('data_test.xml')
    tree = ElementTree.parse(file).getroot()
    return Catalog.from_orm(tree)


@app.get('/tracks', response_model=UserTracks, name='spotify_tracks')
def show_tracks():
    tracks = client.current_user_saved_tracks(limit=50)
    return UserTracks.parse_obj(tracks)


@app.get('/tracks-raw', name='spotify_tracks_raw')
def show_tracks():
    return client.current_user_saved_tracks(limit=50)
