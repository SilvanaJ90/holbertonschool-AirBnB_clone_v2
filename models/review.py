#!/usr/bin/python3
"""Review module for the HBNB project"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """Review classto store review information"""
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
