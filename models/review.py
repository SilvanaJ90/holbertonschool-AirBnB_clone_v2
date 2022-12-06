#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ Review classto store review information """
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""