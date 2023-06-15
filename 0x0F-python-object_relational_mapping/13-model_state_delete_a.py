#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the 
letter a from the database hbtn_0e_6_usa
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
    
    for delete_state in session.query(State).filter(State.name.contains('a')):
        session.delete(delete_state)

    session.commit()
    session.close()
