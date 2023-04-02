#!/usr/bin/env python3
"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        exit(1)

    # Connect to the database
    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects containing the letter "a"
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))