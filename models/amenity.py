#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """The Amenity class, contains state ID and name"""
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

    else:
        name = ""
