#!/bin/bash

# Define location globals
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[@]}" )" && pwd )"
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add bash command for script and install all required programs
function setup() {

	echo "alias api='bash $SCRIPT_DIR/api.sh'" >> $HOME/.bashrc
	source $HOME/.bashrc

	sudo pip install -r $SCRIPT_DIR/requirements.txt

}

# Parse desired action and execute corresponding function
ACTION=$1
case "$ACTION" in
	app)
		bash $SCRIPT_DIR/backend.sh
		;;
	db)
		bash $SCRIPT_DIR/db_gen.sh
		;;
	setup)
		setup
		;;
	*)
		echo "'$ACTION' is not a valid operation."
		echo "Exiting..."
esac
