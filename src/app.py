import json
import xml.etree.ElementTree as ElementTree
from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from loguru import logger as log, logger
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from schemas.atlantmarket import Catalog
from schemas.schemas import Book
from settings_app import config
from settings_log import setup_logger_from_settings
from spotify import client

origins = ['*']
setup_logger_from_settings()


app = FastAPI(
    debug=config.debug,
    title=config.app_name,
    contact=config.contact.dict()
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', name='homepage', include_in_schema=False)
async def homepage():
    logger.debug("hi")
    return RedirectResponse('/docs')


@app.get('/books', response_model=List[Book], name='books')
async def books():
    return Book.all()


@app.get('/catalogs/{id}', response_model=Catalog, name='parsers')
async def item(id: str) -> Catalog:  # noqa
    datas = Path('test_data')
    file = datas.joinpath('data_test.xml')
    tree = ElementTree.parse(file).getroot()
    return Catalog.from_orm(tree)


@app.get('/download-tracks', name='spotify_tracks')
def download_tracks():
    func = client.current_user_saved_tracks
    offset = 0

    def save(page: int):
        data = func(limit=10, offset=page)
        data_dir = Path('data')
        data_dir.mkdir(exist_ok=True, parents=True)
        file = data_dir.joinpath(f'{data.get("offset")}.json')
        with file.open('w') as f:
            f.write(json.dumps(data))
        if data.get('next'):
            save(page + 10)

    save(offset)

    # return UserTracks.parse_obj(tracks)


@app.get('/tracks-raw', name='spotify_tracks_raw')
def show_tracks():
    return client.current_user_saved_tracks(limit=50)
