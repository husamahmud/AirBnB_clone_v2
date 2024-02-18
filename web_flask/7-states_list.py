#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

AirBnB = Flask(__name__)


@AirBnB.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page only if n is an integer"""
    return render_template('7-states_list.html', states=storage.all(State))


@AirBnB.teardown_appcontext
def teardown_db():
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    AirBnB.run(host='0.0.0.0', port=5000)
