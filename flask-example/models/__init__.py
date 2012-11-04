#encoding: utf-8

from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

CURRENT_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))

def pre_connect(filename, debug = False):
    path = "%s/%s" % (CURRENT_DIRECTORY, filename)
    engine = create_engine('sqlite+pysqlite:///%s' % path, module = sqlite, echo = debug)
    SessionMakerInstance = sessionmaker(bind = engine)
    return SessionMakerInstance()

def connect(debug = False):
    return pre_connect("todos.db", debug)
