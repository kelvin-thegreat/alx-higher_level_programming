#!/usr/bin/python3
"""
script  that lists all State objects
from the DB `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    Accessing the DB, getting the states
    from the DB.
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine_create = create_engine(db_url)
    Session_make = sessionmaker(bind=engine_create)

    session = Session_make()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
