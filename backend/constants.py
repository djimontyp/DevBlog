from pathlib import Path

from typing import Literal

# BACKEND
BASE_DIR_BACKEND: Path = Path(__file__).parent
STATIC_BACKEND: Path = BASE_DIR_BACKEND.joinpath('/static')
TEMPLATES_BACKEND: Path = BASE_DIR_BACKEND.joinpath('templates')

# FRONTEND
IMAGES_FRONTEND: Path = Path('images')
BOOKS_FRONTEND: Path = IMAGES_FRONTEND.joinpath('books')

# Spotify
COUNTRIES_CODES = Literal[
    'AD', 'AR', 'AU', 'AT', 'BE', 'BO',
    'BR', 'BG', 'CA', 'CL', 'CO', 'CR',
    'CY', 'CZ', 'DK', 'DO', 'EC', 'SV',
    'EE', 'FI', 'FR', 'DE', 'GR', 'GT',
    'HN', 'HK', 'HU', 'IS', 'ID', 'IE',
    'IT', 'JP', 'LV', 'LI', 'LT', 'LU',
    'MY', 'MT', 'MX', 'MC', 'NL', 'NZ',
    'NI', 'NO', 'PA', 'PY', 'PE', 'PH',
    'PL', 'PT', 'SG', 'ES', 'SK', 'SE',
    'CH', 'TW', 'TR', 'GB', 'US', 'UY'
]
