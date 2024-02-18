#!/usr/bin/python3
"""script to fetch states list from storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

AirBnB = Flask(__name__)


@AirBnB.teardown_appcontext
def teardown(exc):
    """close the session after each request"""
    storage.close()


@AirBnB.route('/states_list', strict_slashes=False)
def states_list():
    """get state list from storage"""
    return render_template("7-states_list.html", states=storage.all(State))


if __name__ == '__main__':
    AirBnB.run(host='0.0.0.0', port=5000)
