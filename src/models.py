import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    created_date = Column(DateTime) 

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    rotation_period = Column(Integer, nullable=False)
    climate = Column (String(250), nullable=True)
    population = Column (Integer, nullable=True)
    url = Column(String(80), unique=True)

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    birth_year= Column(Integer, nullable=True)
    gender = Column (String(250), nullable=True)
    url = Column(String(80), unique=True)


class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    
    
    

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
