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

class TripHikerLink(Base):
    __tablename__ = 'trip_hiker_link'
    trip_id = Column(Integer, ForeignKey('trip.id'), primary_key=True)
    hiker_id = Column(Integer, ForeignKey('hiker.id'), primary_key=True)
    trip = relationship('Trip', backref=backref("hiker_assoc"))
    hiker = relationship('Hiker', backref=backref("trip_assoc"))

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
    expected_return = Column(DateTime())
    trip = relationship('Trip', secondary='trip_hiker_link')

    @property
    def serialize(self):
        return {  # HOW TO UNALPHABETIZE JSON SERIALIZING????
                '1) first_name': self.first_name,
                '2) last_name': self.last_name,
                '3) address': self.address,
                '4) phone_number': self.phone_number,
                '5) email': self.email,
                '6) emergency_contact1': self.emergency_contact1,
                '7) emergency_contact2': self.emergency_contact2,
                '8) expected_return': self.expected_return
        }

class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_name = Column(String(32))
    trip_description = Column(String(800))
    trip_start_location = Column(String(100))
    trip_start_date = Column(DateTime())
    trip_end_location = Column(String(100))
    trip_end_date = Column(DateTime())
    hikers = relationship('Hiker', secondary='trip_hiker_link')

    @property
    def serialize(self):
        return {
                '1. trip_name': self.trip_name,
                '2. trip_description': self.trip_description,
                '3. trip_start_location': self.trip_start_location,
                '4. trip_start_date': self.trip_start_date,
                '5. trip_end_location': self.trip_end_location,
                '6. trip_end_date': self.trip_end_date,
                '7. hikers': [hiker.serialize for hiker in self.hikers]
        }

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
