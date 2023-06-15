#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """
    DB Connection and get a state
    from the database.
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    arizona_state = session.query(State).filter(State.id == '2').first()
    arizona_state.name = 'New Mexico'
    session.commit()
    session.close()
