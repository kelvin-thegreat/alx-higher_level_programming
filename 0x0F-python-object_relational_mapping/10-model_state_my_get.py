#!/usr/bin/python3
"""
Script that prints State objects with the name passed as argument
from DB `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """
    Access to the database and get a state
    
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    first_state = session.query(State).filter(State.name == argv[4]).first()
    if first_state is not None:
        print(f"{first_state.id}")
    else:
        print('Not Found')
