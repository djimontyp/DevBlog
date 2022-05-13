from pathlib import Path

# BACKEND
BASE_DIR_BACKEND: Path = Path(__file__).parent
STATIC_BACKEND: Path = BASE_DIR_BACKEND.joinpath('/static')
TEMPLATES_BACKEND: Path = BASE_DIR_BACKEND.joinpath('templates')

# FRONTEND
IMAGES_FRONTEND: Path = Path('images')
BOOKS_FRONTEND: Path = IMAGES_FRONTEND.joinpath('books')

