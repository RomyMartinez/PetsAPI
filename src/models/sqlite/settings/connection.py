from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

db_conection_handler = DBConnectionHandler()
