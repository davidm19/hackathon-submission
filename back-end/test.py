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

if __name__ == "__main__":
    unittest.main()
