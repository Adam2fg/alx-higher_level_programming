#!/usr/bin/env python3
"""Script that lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == '__main__':
    # Gather MySQL credentials
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Setup connection with database using SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username,
            mysql_password,
            database_name
        ),
        pool_pre_ping=True
    )

    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query to retrieve all City objects and related State objects
    cities = session.query(City).order_by(City.id.asc()).all()

    # Print City and State information
    for city in cities:
        print("{}: {} -> {}".format(
            city.id,
            city.name,
            city.state.name
        ))

    # Close the session
    session.close()
