from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from database import db
from schemas import CountryCode

auth_manager = SpotifyOAuth(
    client_id='0aa505304fb3415a9b52df7ab67db1c7',
    client_secret='afe4be1035bc4248a39c43bd9e4079f7',
    scope='user-library-read',
    redirect_uri='http://0.0.0.0:7555/'
)

client = Spotify(auth_manager=auth_manager)


def fill_const():
    with db.get_session() as s:
        codes = [CountryCode(code=code) for code in client.country_codes]
        s.add_all(codes)
        s.commit()
