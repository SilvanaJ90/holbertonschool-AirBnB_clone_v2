#!/usr/bin/python
""" Doc """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
"""from models.user import User"""
"""from models.place import Place"""
from models.state import State
from models.city import City
"""from models.amenity import Amenity"""
"""from models.review import Review"""
import os


classes = {
            """'User': User, 'Place': Place, 'Amenity': Amenity, 'Review': Review,"""
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
        self.__engine = create_engine("mysql+mysqldb://{:s}:{:s}@{:s}/{:s}".format(
                                    user, pwd, host, db), pool_pre_ping=True)

        metaData = MetaData()
        if os.getenv('HBNB_ENV') == 'test':
            metaData.drop_all()

    def all(self, cls=None):
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """ Add obj to session"""
        self.__session.add(obj)

    def save(self, obj):
        """ Save tables of DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes tables of DB"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables of DB """
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker, scoped_session
        """from models.user import User
        from models.place import Place"""
        from models.state import State
        from models.city import City
        f"""rom models.amenity import Amenity
        from models.review import Review"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

        

        def close(self):
            Session.close(self.__session)