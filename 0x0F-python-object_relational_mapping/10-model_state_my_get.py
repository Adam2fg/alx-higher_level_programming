#!/usr/bin/env python3
"""
Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>".format(sys.argv[0]))
        exit(1)

    # Connect to the database
    username, password, database, state_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve State object with the given name
    state = session.query(State).filter_by(name=state_name).first()

    # Print results
    if state is None:
        print("Not found")
    else:
        print(state.id)