#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

env = getenv('HBNB_TYPE_STORAGE')

place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if env == "db":
        reviews = relationship(
                "Review", backref="place", cascade="all, delete")
        amenities = relationship(
                "Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")
    else:
        pass
