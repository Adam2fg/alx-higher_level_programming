#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # create the connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a session to connect to the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # update the name of the State where id = 2 to New Mexico
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = 'New Mexico'
        session.commit()

    # close the session
    session.close()