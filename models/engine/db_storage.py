#!/usr/bin/python3
"""This module defines a base class for managing DB storage in hbnb clone"""
import json
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class defines a base class for managing DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Init the DBStorage class"""
        dialect = 'mysql'
        driver = 'mysqldb'
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            '{]+{}://{}:{}@{}/{}'.format(dialect,
                                         driver,
                                         HBNB_MYSQL_USER,
                                         HBNB_MYSQL_PWD,
                                         HBNB_MYSQL_HOST,
                                         HBNB_MYSQL_DB,
                                         pool_pre_ping=True))
        if HBNB_ENV == 'test':
            self.__engine = Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Get all DB storage"""
        dic = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                dic[f"{obj.__class__.__name__}.{obj.id}"] = obj
            return dic

        classes = [State, City, User, Place]
        for model in classes:
            for obj in self.__session.query(model).all():
                dic[f"{model.__name__}.{obj.id}"] = obj

    def new(self, obj):
        """Create new DB storage"""
        self.__session.add(obj)

    def save(self):
        """Save DB storage"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete DB storage"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload DB storage"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """Close DB storage"""
        self.__session.close()
