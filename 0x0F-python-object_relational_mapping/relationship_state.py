#!/usr/bin/python3

"""
Script that defines a State and a Base class to work with MySQLAlchemy ORM.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """
    State class

    Attributes:
        __tablename__ (str): tablename of the class
        id (int): The State id
        name (str): The State name
        cities (:obj:'city'): belongs to the state

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
