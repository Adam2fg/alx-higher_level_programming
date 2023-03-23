#!/usr/bin/python3
"""
This script demonstrates how to use the State class defined in model_state.py
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database',
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example usage: Add a new state to the database
    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    # Close session and database connection
    session.close()