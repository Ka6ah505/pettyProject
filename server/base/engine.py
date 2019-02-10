from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

class Engine():

    def __init__(self):
        connect = create_engine('sqlite:////app.db', convert_unicode=True)
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                                      autoflush=False,
                                                      bind=connect))


    def getPerson(self, id=None):
        pass
