#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    City class that inherits from Base.
    Represents the cities table in the MySQL database hbtn_0e_100_usa.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship(State, backref="cities")

    def __str__(self):
        """
        Return a string representation of the City object.
        """
        return "{}: ({}) {}".format(self.state.name, self.id, self.name)