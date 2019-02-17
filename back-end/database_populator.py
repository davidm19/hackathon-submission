from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Trip, engine
from datetime import datetime
import argparse

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

<<<<<<< HEAD
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
=======
hiker1 = Hiker(first_name="Michael", last_name="Bluth",
               address="The model home", phone_number="12223334444",
               emergency_contact1="Lucille Bluth", emergency_contact2=None,
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker2 = Hiker(first_name="GOB", last_name="Bluth",
               address="The model home", phone_number="13334445555",
               emergency_contact1="Lucille Bluth",
               emergency_contact2="Michael Bluth",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker3 = Hiker(first_name="Lindsay", last_name="Bluth-Funke",
               address="The model home", phone_number="14445556767",
               emergency_contact1="Lucille Bluth",
               emergency_contact2="Michael Bluth",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker4 = Hiker(first_name="Buster", last_name="Bluth",
               address="The model home", phone_number="55567678999",
               emergency_contact1="Lucille Bluth",
               emergency_contact2="Mother",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker5 = Hiker(first_name="Tobias", last_name="Funke",
               address="The model home", phone_number="14209696969",
               emergency_contact1="Lindsay Bluth-Funke",
               emergency_contact2="Michael Bluth",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker6 = Hiker(first_name="Lucille", last_name="Bluth",
               address="123 Ocean View Appartments Unit 42",
               phone_number="19998887777",
               emergency_contact1="George Bluth Sr.",
               emergency_contact2="Oscar Bluth",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker7 = Hiker(first_name="George", last_name="Bluth",
               address="Orange County Prison",
               phone_number="18887776565",
               emergency_contact1="Lucille Bluth",
               emergency_contact2="GOB Bluth",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker8 = Hiker(first_name="Oscar", last_name="Bluth",
               address="123 Ocean View Appartments Unit 42",
               phone_number="17776565555",
               emergency_contact1="Lucille Bluth",
               emergency_contact2=None,
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker9 = Hiker(first_name="George-Michael", last_name="Bluth",
               address="The model home",
               phone_number="12223334444",
               emergency_contact1="Michael Bluth",
               emergency_contact2="Lindsay Bluth",
               expected_return=datetime(2019, 2, 22, 16, 30))
hiker10 = Hiker(first_name="Maeby", last_name="Funke",
                address="The model home",
                phone_number="13334445555",
                emergency_contact1="Lindsay Bluth-Funke",
                emergency_contact2="Tobias Funke",
                expected_return=datetime(2019, 2, 22, 16, 30))

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
>>>>>>> david/back-end
session.commit()
# trip1.hikers.append(hiker1)
# trip1.hikers.append(hiker2)
# trip1.hikers.append(hiker3)
# trip1.hikers.append(hiker4)
# session.add(trip1)
# session.commit()
