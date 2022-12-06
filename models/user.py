"""user Module for HBNB project """
from models.base_model import BaseModel, Base
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ Place class """
    if HBNB_TYPE_STORAGE == 'db':
        '''User class'''
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Places", backref="user", cascade="all, delete")
        reviews = relationship("review", backref="user", cascade="all,delete")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""