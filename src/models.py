import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class StarWars(Base):
    __tablename__ = 'StarWars'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Characters = Column(String(250), nullable=False)
    Planets = Column(String(250), nullable=False)
    Starships = Column(String(250), nullable=False)
    Favourites = Column(String(250), nullable=False)
    

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Name = Column(String(250), ForeignKey('StarWars.ID'), ForeignKey('Favourites_Character.ID'))
    Description = Column(String(250), nullable=False)
    Created = Column(String(250), nullable=False)
    Gender = Column(String(250), nullable=False)
    Eye_Color = Column(String(250), nullable=False)
    Hair_Color = Column(String(250), nullable=False)
    StarWars = relationship(StarWars)
    
    

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Name = Column(String(250), ForeignKey('StarWars.ID'), ForeignKey('Favourites_Planet.ID'))
    Description = Column(String(250), nullable=False)
    Created = Column(String(250), nullable=False)
    Climate = Column(String(250), nullable=False)
    Terrain = Column(String(250), nullable=False)
    StarWars = relationship(StarWars)
   

class Starships(Base):
    __tablename__ = 'Starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Model = Column(String(250), ForeignKey('StarWars.ID'), ForeignKey('Favourites_Starship.ID'))
    Description = Column(String(250), nullable=False)
    Starship_Class = Column(String(250), nullable=False)
    Manufacturer = Column(String(250), nullable=False)
    Max_Atmosphering_Speed = Column(String(250), nullable=False)
    StarWars = relationship(StarWars)
   

class Favourites_Character(Base):
    __tablename__ = 'Favourites_Character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Character_Name = Column(String(250), ForeignKey('Characters.ID'), ForeignKey('StarWars.ID'))
    Characters = relationship(Characters)
    StarWars = relationship(StarWars)

class Favourites_Planet(Base):
    __tablename__ = 'Favourites_Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Planet_Name = Column(String(250), ForeignKey('Planets.ID'), ForeignKey('StarWars.ID'))
    Planets = relationship(Planets)
    StarWars = relationship(StarWars)

class Favourites_Starship(Base):
    __tablename__ = 'Favourites_Starship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Starship_Name = Column(String(250), ForeignKey('Starships.ID'), ForeignKey('StarWars.ID'))
    Starships = relationship(Starships)
    StarWars = relationship(StarWars)

   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e