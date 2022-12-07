#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import  relationship, backref
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """The city class, contains state ID and name"""
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place",backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""
