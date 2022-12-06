#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os
from sqlalchemy.orm import relationship, backref

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ The city class, contains state ID and name """
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            "Place relationship",
            backref=backref("cities", cascade="all"),
            cascade="all",
            passive_deletes=True)
    else:
        state_id = ""
        name = ""
