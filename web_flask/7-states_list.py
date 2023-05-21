#!/usr/bin/python3
"""
Module to run an instance of AirBnB Clone with Flask
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ Method to list all states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception=None):
    """ Function to remove current SQLalchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
