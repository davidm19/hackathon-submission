from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Trip, Hiker, engine
import argparse

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name="Michael", last_name="Huang", grade="7")
hiker1 = Hiker
session.add(student1)
session.commit()

trip1 = Trip(trip_name="Death Valley Backpacking", trip_grade="9")
session.add(trip1)
session.commit()
