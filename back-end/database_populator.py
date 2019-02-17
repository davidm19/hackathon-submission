from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Trip, engine
from datetime import datetime
import argparse

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# hiker1 = Hiker(first_name="Sam", last_name="Jamjar", address="123 Sesame Street", phone_number="12223334444", email="sjamjar@gmail.com", emergency_contact1="mommy", emergency_contact2="daddy", expected_return=datetime(2019, 2, 22, 16, 30))
# hiker2 = Hiker(first_name="Anna", last_name="McIntosh", address="456 Applebee Avenue", phone_number="15556778899", email="anna.mc@gmail.com", emergency_contact1="mama", emergency_contact2="papa", expected_return=datetime(2019, 2, 22, 16, 30))
# hiker3 = Hiker(first_name="Buster", last_name="Bluth", address="Mom's appartment", phone_number="12345675432", email="lucille.bluth@gmail.com", emergency_contact1="Lucille Bluth", emergency_contact2="Mother", expected_return=datetime(2019, 2, 22, 16, 30))
# hiker4 = Hiker(first_name="Tobias", last_name="Funke", address="The Model Home", phone_number="19873276543", email="ibluemyselfforthis@gmail.com", emergency_contact1="Lindsay Bluth", emergency_contact2="Michael Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
# session.add(hiker1)
# session.add(hiker2)
# session.add(hiker3)
# session.add(hiker4)
# session.commit()

trip1 = Trip(trip_name="Big Loop around the Small Pond", trip_description="A big loop around a small pond")
trip2 = Trip(trip_name="Waterfall Hike", trip_description="A hike to the waterfall off in yonder distance")
trip3 = Trip(trip_name="Devil's Postpile", trip_description="A hike to Devil's Postpile")
trip4 = Trip(trip_name="Rainbow Lake", trip_description="A hike to rainbow lake")
trip5 = Trip(trip_name="Convict Lake Loop", trip_description="A hike around the loop around Convict Lake")
trip6 = Trip(trip_name="Running trail", trip_description="A run around the trail")
trip7 = Trip(trip_name="A trip", trip_description="A trip")
trip8 = Trip(trip_name="Joshua Tree loop", trip_description="A big loop around Joshua Tree")
session.add(trip1)
session.add(trip2)
session.add(trip3)
session.add(trip4)
session.add(trip5)
session.add(trip6)
session.add(trip7)
session.add(trip8)
session.commit()
# trip1.hikers.append(hiker1)
# trip1.hikers.append(hiker2)
# trip1.hikers.append(hiker3)
# trip1.hikers.append(hiker4)
# session.add(trip1)
# session.commit()
