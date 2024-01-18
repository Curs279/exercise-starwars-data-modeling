import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base): # parent
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False, )
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    users = relationship("Favorites")

class Favorites(Base): # children
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="users")
    id_characters = Column(Integer, ForeignKey('characters.id'))
    characters = relationship("Characters")
    id_planets = Column(Integer, ForeignKey('planets.id'))
    planets = relationship("Planets")
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship("Vehicles")

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(20))
    height = Column(Integer)
    
class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    favorites = relationship("Favorites")

class Vehicles(Base):
    __tablename__ ='vehicles'

    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    make = Column(String(100))
    vehicle_class = Column(String(100))
    passengers = Column(Integer)



render_er(Base, 'diagram.png')