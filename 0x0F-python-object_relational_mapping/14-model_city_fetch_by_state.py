#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
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

    # query all City objects and sort them by id
    cities = session.query(City).order_by(City.id).all()

    # print the results
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # close the session
    session.close()
