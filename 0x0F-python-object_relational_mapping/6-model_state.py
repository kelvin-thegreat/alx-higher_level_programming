#!/usr/bin/python3

"""
Script that defines a State and a Base class to work with MySQLAlchemy ORM.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class

    Attributes:
        __tablename__ (str): tablename of the class
        id (int): The State id
        name (str): The State name

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
