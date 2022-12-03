#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
import os


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class User(BaseModel):
    """This class defines a user by various attributes"""
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
