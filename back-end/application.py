import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Hiker, engine, Trip, TripHikerLink
from flask import session as login_session
import random
import string
import json
from flask import make_response
from sqlalchemy.sql import exists
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

APPLICATION_NAME = "Hiking Safety App"

# SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']
# engine = create_engine('sqlite:///SQLALCHEMY_DATABASE_URI.db')
engine = create_engine('sqlite:///database.db?check_same_thread=false')

DBSession = sessionmaker(bind=engine)

session = DBSession()


@app.route('/')
def show_hostpage():
    return "Hostpage"


@app.route('/trips', methods=['GET'])
def getTrips():
    tripList = []
    allTrips = session.query(Trip).all()
    for trip in allTrips:
        trip_info = {"trip_name": trip.trip_name,
                     "id": trip.id,
                     "trip_description": trip.trip_description,
                     "trip_start_location": trip.trip_start_location,
                     "trip_start_date": trip.trip_start_date,
                     "trip_end_location": trip.trip_end_location,
                     "trip_end_date": trip.trip_end_date,

                     }
        tripList.append(trip_info)
    return flask.jsonify(tripList), 200


@app.route('/trips/<int:trip_id>/detail', methods=['GET'])
def showTrip(trip_id):
    trip = session.query(Trip).filter_by(id=trip_id).one()
    trip_info = {"trip_name": trip.trip_name,
                 "id": trip.id,
                 "trip_description": trip.trip_description,
                 "trip_start_location": trip.trip_start_location,
                 "trip_start_date": trip.trip_start_date,
                 "trip_end_location": trip.trip_end_location,
                 "trip_end_date": trip.trip_end_date,
                  }
    return flask.jsonify(trip_info), 200


@app.route('/trips/new', methods=['POST'])
def addTrip():
    post = request.get_json()
    if request.method == 'POST':
        new_trip = Trip(trip_name=post["trip_name"],
                        trip_description=post["trip_description"],
                        trip_start_location=post["trip_start_location"],
                        trip_start_date=post["trip_start_date"],
                        trip_end_location=post["trip_end_location"],
                        trip_end_date=post["trip_end_date"])
    session.add(new_trip)
    session.commit()
    return flask.jsonify("successfully created new trip"), 200


@app.route('/trips/<int:id>/update', methods=['PUT'])
def updateTrip(id):
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    trip_id = post["id"]
    edited_trip = session.query(Trip).filter_by(id=trip_id).one()
    if "trip_name" in post:
        edited_trip.trip_name = post["trip_name"]
    session.add(edited_trip)
    session.commit()
    return flask.jsonify("Trip successfully updated! \n"), 200


@app.route('/trips/<int:trip_id>/delete', methods=['DELETE'])
def deleteTrip(trip_id):
    post = request.get_json()
    trip_to_delete = session.query(Trip).filter_by(id=trip_id).one()
    session.delete(trip_to_delete)
    session.commit()
    return flask.jsonify("Trip successfully deleted!"), 200

@app.route('/trips/<int:trip_id>/detail/hikers', methods=['GET'])
def getHikersInTrip(trip_id):
    tripHikerList = []
    tripHikerLinks = session.query(TripHikerLink).join(Trip).filter(Trip.id == trip_id).all()
    for tripHikerLink in tripHikerLinks:
        hiker_info = {"first_name": tripHikerLink.hiker.first_name,
                      "last_name": tripHikerLink.hiker.last_name,
                      "address": tripHikerLink.hiker.address,
                      "phone_number": tripHikerLink.hiker.phone_number,
                      "email": tripHikerLink.hiker.email,
                      "emergency_contact1": tripHikerLink.hiker.emergency_contact1,
                      "emergency_contact2": tripHikerLink.hiker.emergency_contact2,
                      "expected_return": tripHikerLink.hiker.expected_return,
                      }
        tripHikerList.append(hiker_info)
    print(tripHikerList);
    return flask.jsonify(tripHikerList), 200

@app.route('/hikers/<int:hiker_id>', methods=['GET'])
def showHiker(hiker_id):
    hiker = session.query(Hiker).filter_by(id=hiker_id).one()
    hiker_info = {"first_name": hiker.first_name,
                  "last_name": hiker.last_name,
                  "address": hiker.address,
                  "phone_number": hiker.phone_number,
                  "email": hiker.email,
                  "emergency_contact1": hiker.emergency_contact1,
                  "emergency_contact2": hiker.emergency_contact2,
                  "expected_return": hiker.expected_return,
                }
    return flask.jsonify(hiker_info), 200

@app.route('/hikers', methods=['GET'])
def getHikers():
    hikerList = []
    allHikers = session.query(Hiker).all()
    for hiker in allHikers:
        hiker_info = {"first_name": hiker.first_name,
                      "last_name": hiker.last_name,
                      "address": hiker.address,
                      "phone_number": hiker.phone_number,
                      "email": hiker.email,
                      "emergency_contact1": hiker.emergency_contact1,
                      "emergency_contact2": hiker.emergency_contact2,
                      "expected_return": hiker.expected_return,
                    }
        hikerList.append(hiker_info)
    return flask.jsonify(hikerList), 200

@app.route('/hikers/new', methods=['POST'])
def newHiker():
    post = request.get_json()
    if request.method == 'POST':
        newHiker = Hiker(first_name=post["first_name"],
                          last_name=post["last_name"],
                          address=post["address"],
                          phone_number=post["phone_number"],
                          email=post["email"],
                          emergency_contact1=post["emergency_contact1"],
                          emergency_contact2=post["emergency_contact2"],
                          expected_return=post["expected_return"]
                          )
    session.add(newHiker)
    session.commit()
    return flask.jsonify("Hiker successfully added! \n"), 200


@app.route('/hikers/<int:id>/edit', methods=['PUT'])
def editHiker(id):
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    hiker_id = post["id"]
    edited_hiker = session.query(Hiker).filter_by(id=hiker_id).one()
    if 'first_name' in post:
        edited_hiker.first_name = post['first_name']
    elif 'last_name' in post:
        edited_hiker.last_name = post['last_name']
    elif 'address' in post:
        edited_hiker.address = post['address']
    elif 'phone_number' in post:
        edited_hiker.phone_number = post['address']
    elif 'email' in post:
        edited_hiker.email = post['email']
    elif 'emergency_contact1' in post:
        edited_hiker.emergency_contact1 = post['emergency_contact1']
    elif 'emergency_contact2' in post:
        edited_hiker.emergency_contact2 = post['emergency_contact2']
    elif 'expected_return' in post:
        edited_hiker.expected_return = post['expected_return']
    session.add(edited_hiker)
    session.commit()
    return flask.jsonify("Hiker successfully updated! \n"), 200


@app.route('/hikers/<int:id>/delete', methods=['PUT'])
def deleteHiker(id):
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    hiker_id = post["id"]
    hiker_to_delete = session.query(Hiker).filter_by(id=id).one()
    session.delete(hiker_to_delete)
    session.commit()
    return flask.jsonify("Hiker successfully deleted! \n"), 200


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
