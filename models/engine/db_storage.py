from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

        if cls is None:
            result = self.__session.query(User, State, City, Amenity, Place, Review).all()
            dictionary = {}
            for obj in result:
                dictionary.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return dictionary
        else:
            obj = self.__session.query(cls).all()
            return {obj.to_dict()['__class__'] + '.' + obj.id: obj}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base = declarative_base()
        Base.metadata.create_all(self.__engine)
