#!/usr/bin/python3
"""
Script that lists all State objects containing letter 'a' from DB `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    for first_state in session.query(State).filter(State.name.contains('a')):
        print(f"{first_state.id}: {first_state.name}")

