#!/usr/bin/python3
"""
Script that prints the first State object ifrom the DB `hbtn_0e_6_usa`.
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
    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

