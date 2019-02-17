# project/test_basic.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from database_setup import Base, Hiker, Trip, engine
# from test_database_setup import Trip
import os
import unittest
import datetime
from application import *
from application import session, app
from flask import json

app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class BasicTests(unittest.TestCase):

    def test_is_overdue(self):
        # with app.app_context():
        results = is_overdue(1)
        expected_results = True
        self.assertEqual(results, expected_results)

    def test_new_hiker(self):
        with app.app_context():
            expected_results = {'1) first_name': "Michael",
                                '2) last_name': "Bluth",
                                '3) address': "The  model home",
                                '4) phone_number': "12223334444",
                                '5) emergency_contact1': "Lucille Bluth",
                                '6) emergency_contact2': None,
                                '7) expected_return': "some date"
                                }
            results = show_hiker(1)
            response_json = json.loads(results[0].data.decode('utf-8'))
            self.assertEqual(response_json, expected_results)

if __name__ == "__main__":
    unittest.main()
