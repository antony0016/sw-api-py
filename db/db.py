from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DB:
    def __init__(self, db_user, db_password, db_host, db_port, db_name):
        self.connection_string = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.engine = create_engine(self.connection_string)

    def get_engine(self):
        return self.engine

    def get_session(self):
        return Session(self.engine)
