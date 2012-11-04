#encoding: utf-8

from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os, inspect   

CURRENT_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))
DATABASE_NAME = "todos.db"

# Classe de base dont nos models doivent hériter pour avoir la magie
# de SQLAlchemy. Sert également pour la génération automatisé de la BD dans
# la fonction init_db
Base = declarative_base()

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
    engine = create_engine('sqlite:///%s' % path, convert_unicode=True)
    Base.metadata.create_all(bind=engine)
