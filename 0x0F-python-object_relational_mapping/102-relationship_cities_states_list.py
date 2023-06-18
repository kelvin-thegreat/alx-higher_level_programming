#!/usr/bin/python3
"""
Module to List all City objects from DB hbtn_0e_101_usa
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),pool_pre_ping=True)
    
Base.metadata.create_all(engine)
Se = sessionmaker(bind=engine)
se = Se()

states = se.query(State).join(City).order_by(City.id).all()
for state in states:
    for city in state.cities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
