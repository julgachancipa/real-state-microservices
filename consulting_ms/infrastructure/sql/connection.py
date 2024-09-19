import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from settings import Settings
from utils.singleton import Singleton

settings = Settings()


class Connection(metaclass=Singleton):
    def __init__(self):
        engine = db.create_engine(settings.DB_URI)
        session = sessionmaker(bind=engine)
        self.session = session()
