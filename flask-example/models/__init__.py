#encoding: utf-8

from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os, inspect   

CURRENT_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))
DATABASE_NAME = "todos.db"

def pre_connect(filename, debug = False):
    path = "%s/%s" % (CURRENT_DIRECTORY, filename)
    engine = create_engine('sqlite+pysqlite:///%s' % path, module = sqlite, echo = debug)
    SessionMakerInstance = sessionmaker(bind = engine)
    return SessionMakerInstance()

def connect(debug = False):
    return pre_connect(DATABASE_NAME, debug)

def init_db():
    """
        Créateur de la bd SQLite
    """
    from todo import Todo

    path = "%s/%s" % (CURRENT_DIRECTORY, DATABASE_NAME)
    engine = create_engine('sqlite+pysqlite:///%s' % path, convert_unicode=True)
    Base = declarative_base()

    Base.metadata.create_all(bind=engine)