from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Trip, Hiker, engine
from datetime import datetime
import argparse

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

hiker1 = Hiker(first_name="Michael", last_name="Bluth", address="The model home", phone_number="12223334444", emergency_contact1="Lucille Bluth", emergency_contact2=None, expected_return=datetime(2019, 2, 22, 16, 30))
hiker2 = Hiker(first_name="GOB", last_name="Bluth", address="The model home", phone_number="13334445555", emergency_contact1="Lucille Bluth", emergency_contact2="Michael Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
hiker3 = Hiker(first_name="Lindsay", last_name="Bluth-Funke", address="The model home", phone_number="14445556767", emergency_contact1="Lucille Bluth", emergency_contact2="Michael Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
hiker4 = Hiker(first_name="Buster", last_name="Bluth", address="The model home", phone_number="55567678999", emergency_contact1="Lucille Bluth", emergency_contact2="Mother", expected_return=datetime(2019, 2, 22, 16, 30))
hiker5 = Hiker(first_name="Tobias", last_name="Funke", address="The model home", phone_number="14209696969", emergency_contact1="Lindsay Bluth-Funke", emergency_contact2="Michael Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
hiker6 = Hiker(first_name="Lucille", last_name="Bluth", address="123 Ocean View Appartments Unit 42", phone_number="19998887777", emergency_contact1="George Bluth Sr.", emergency_contact2="Oscar Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
hiker7 = Hiker(first_name="George", last_name="Bluth", address="Orange County Prison", phone_number="18887776565", emergency_contact1="Lucille Bluth", emergency_contact2="GOB Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
hiker8 = Hiker(first_name="Oscar", last_name="Bluth", address="123 Ocean View Appartments Unit 42", phone_number="17776565555", emergency_contact1="Lucille Bluth", emergency_contact2=None, expected_return=datetime(2019, 2, 22, 16, 30))
hiker9 = Hiker(first_name="George-Michael", last_name="Bluth", address="The model home", phone_number="12223334444", emergency_contact1="Michael Bluth", emergency_contact2="Lindsay Bluth", expected_return=datetime(2019, 2, 22, 16, 30))
hiker10 = Hiker(first_name="Maeby", last_name="Funke", address="The model home", phone_number="13334445555", emergency_contact1="Lindsay Bluth-Funke", emergency_contact2="Tobias Funke", expected_return=datetime(2019, 2, 22, 16, 30))

session.add(hiker1)
session.add(hiker2)
session.add(hiker3)
session.add(hiker4)
session.add(hiker5)
session.add(hiker6)
session.add(hiker7)
session.add(hiker8)
session.add(hiker9)
session.add(hiker10)
session.commit()

trip1 = Trip(trip_name="There's always money in the banana stand")
trip1.hikers.append(hiker1)
trip1.hikers.append(hiker2)
trip1.hikers.append(hiker3)
trip1.hikers.append(hiker4)
trip1.hikers.append(hiker5)

trip2 = Trip(trip_name="I just blew myself")
trip2.hikers.append(hiker1)
trip2.hikers.append(hiker2)
trip2.hikers.append(hiker3)
trip2.hikers.append(hiker4)
trip2.hikers.append(hiker5)

session.add(trip1)
session.add(trip2)
session.commit()
