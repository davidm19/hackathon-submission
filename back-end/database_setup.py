import sys
import os
import argparse
from sqlalchemy import Table, Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('hiker_id', Integer, 
                              ForeignKey('hiker.id')), 
                          Column('trip_id', Integer, 
                              ForeignKey('trip.id'))
                          )

class Hiker(Base):
    __tablename__ = 'hiker'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    address = Column(String(32))
    phone_number = Column(String(32))
    email = Column(String(32))
    emergency_contact1 = Column(String(32))
    emergency_contact2 = Column(String(32))
    expected_return = Column(DateTime()) # WHENEVER WE WANT TO ESTABLISH A DATE, YOU HAVE TO PASS IT IN
    trip = relationship('Trip', secondary=association_table, back_populates="hikers")

    @property
    def serialize(self):
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'address': self.address,
                'phone_number': self.phone_number,
                'emergency_contact1': self.emergency_contact1,
                'emergency_contact2': self.emergency_contact2,
                'expected_return': self.expected_return
        }

class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_name = Column(String(32))
    hikers = relationship('Hiker', secondary=association_table, back_populates="trip")

# parser = argparse.ArgumentParser()
# parser.add_argument("-t", "--test", action="store_true")
# args = parser.parse_args()
# if args.test:
#     print "Created test database"
#     engine = create_engine('sqlite:///test.db')
# else:
#     print "Created regular database"
#     engine = create_engine('sqlite:///database.db')

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# information (name, contact info, expected checkout date) and trips (groups of hikers)
