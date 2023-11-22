from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
        user, password, host, database), pool_pre_ping=True)

        if env == 'test':
            pass

    def all(self, cls=None):
        if cls is None:
            # If cls is not specified, query all objects from all tables
            objects = self.__session.query(State, City, Amenity, Place, Review, User).all()
        else:
            # Query all objects of the specified class
            objects = self.__session.query(State).all()

        return {f'{obj.__class__.__name__}.{obj.id}': obj for obj in objects}


    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        