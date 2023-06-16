#!/usr/bin/python3
"""
This script defines a City class working with MySQLAlchemy ORM.

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    classs City
    Attributes:
        __tablename__ (str): The table name.
        id (int): The id.
        name (str): The name.
        state_id (int): The state the city.

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
