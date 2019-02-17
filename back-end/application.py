import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Hiker, engine, Trip
# from database_setup import Trip
from flask import session as login_session
import random
import string
import json
from flask import make_response
from sqlalchemy.sql import exists
import os
# from flask_cors import CORS

app = Flask(__name__)

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
def show_trips():
    trip_list = []
    all_trips = session.query(Trip).all()
    for trip in all_trips:
        trip_list.append(trip.serialize)
    return flask.jsonify(trip_list), 200


@app.route('/trips/<int:trip_id>/detail', methods=['GET'])
def show_trip(trip_id):
    trip = session.query(Trip).filter_by(id=trip_id).one()
    return flask.jsonify(trip.serialize), 200


@app.route('/trips/new', methods=['POST'])
def add_trip():
    post = request.get_json()
    if request.method == 'POST':
        new_trip = Trip(trip_name=post["trip_name"])
    session.add(newTrip)
    session.commit()
    return flask.jsonify("Trip successfully added!"), 200


@app.route('/trips/<int:id>/update', methods=['PUT'])
def update_trip(id):
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
def delete_trip(trip_id):
    post = request.get_json()
    trip_to_delete = session.query(Trip).filter_by(id=trip_id).one()
    session.delete(trip_to_delete)
    session.commit()
    return flask.jsonify("Trip successfully deleted!"), 200



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
