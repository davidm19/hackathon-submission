#!/bin/bash

# If there is a test database already present, delete it
if [[ -e database.db ]]; then
	rm database.db
fi

# Create new test database and populate it
echo -e "*** SETTING UP TEST DATABASE ***" 
python database_setup.py
echo -e "\n*** POPULATING DATABASE ***"
python database_populator.py

# Run the application
echo -e "\n*** RUNNING SERVER ***"
python application.py
