#!/usr/bin/python3
""" Doc """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from sqlalchemy.orm import Session
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
import os
from models.amenity import Amenity
from models.review import Review


classes = {
            'User': User,
            'Place': Place, 'Amenity': Amenity, 'Review': Review,
            'State': State, 'City': City
            }


class DBStorage:
    """ Doc """

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            "mysql+mysqldb://{:s}:{:s}@{:s}/{:s}".format(
                                    user, pwd, host, db), pool_pre_ping=True)

        metaData = MetaData()
        if os.getenv('HBNB_ENV') == 'test':
            metaData.drop_all()

    def all(self, cls=None):
        self.__session = Session(self.__engine)
        ret_dict = dict()
        if cls:
            for obj in self.__session.query(cls).all():
                ret_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            class_list = [User, State, City, Place, Review, Amenity]
            for query_cls in class_list:
                for obj in self.__session.query(query_cls).all():
                    ret_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return ret_dict

    def new(self, obj):
        """Doc"""
        self.__session.add(obj)

    def save(self):
        """Doc"""
        self.__session.commit()

    def delete(self, obj=None):
        """Doc"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Doc"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        Session.close(self.__session)
