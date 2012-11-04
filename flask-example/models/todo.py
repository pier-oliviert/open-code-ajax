#encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Todo(Base): 
    id = Column("id", Integer, primary_key = True)
    title = Column("title", String(100))
    done = Column("done", Boolean, default = False)
    
    def __unicode__(self):
        print self.title