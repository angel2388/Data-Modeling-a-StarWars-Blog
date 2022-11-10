import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Apellidos = Column(String(250))
    Email = Column(String(250))
    Nick = Column(String(250))
    Contraseña = Column(String(250))
    



class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
   

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    


    def to_dict(self):
        return {}


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer,ForeignKey('planetas'))
    planetas = relationship(Planetas)
    personaje_id = Column(Integer,ForeignKey('personajes'))
    personajes = relationship(Personajes)
    vehiculo_id = Column(Integer,ForeignKey('vehiculos'))
    vehiculos = relationship(Vehiculos)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')