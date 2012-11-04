#coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean
from . import Base

class Todo(Base): 
    __tablename__ = "todo"
    id = Column("id", Integer, primary_key = True)
    title = Column("title", String(100))
    done = Column("done", Boolean, default = False)
    
    def __unicode__(self):
        print self.title