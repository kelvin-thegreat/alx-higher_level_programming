#!/usr/bin/python3
""" 
This script prints all City objects 
from the database `hbtn_0e_14_usa`. 
"""

from relationship_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    """ 
    Connecting the DB and 
    get the cities from the DB. 
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()
