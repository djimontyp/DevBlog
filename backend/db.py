from contextlib import contextmanager

from sqlmodel import SQLModel, create_engine, Session

from config import dev_settings
from schemas import *  # noqa Define schemas in SQLModel


class DataBase:
    def __init__(self, settings):
        self.engine = create_engine(settings.DB_URL, echo=True)

    @contextmanager
    def get_session(self):
        session = Session(self.engine)
        try:
            yield session
        finally:
            session.close()

    def init(self):
        SQLModel.metadata.create_all(self.engine)

    def drop(self):
        SQLModel.metadata.drop_all(self.engine)

    def __repr__(self):
        return f"{self.engine}"


db = DataBase(dev_settings)
