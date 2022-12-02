#!/usr/bin/python
""" Doc """
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
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
        """constructor DBStorage object"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB
        ), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engi

    def all(self, cls=None):
        self.__session = Session(self.__engine)
        ret_dict = dict()
        if cls:
            for obj in self.__session.query(cls).all():
                ret_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            class_list = [State, City]
            for query_cls in class_list:
                for obj in self.__session.query(query_cls).all():
                    ret_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return ret_dict

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