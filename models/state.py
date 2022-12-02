#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object): 
    """ State class """
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            from models.city import City
            from models import storage
            city_obj = storage.all(City)
            return [city for city in city_obj.values() if city.state_id == self.id]