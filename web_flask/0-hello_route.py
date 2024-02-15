#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

AirBnB = Flask(__name__)


@AirBnB.route('/', strict_slashes=False)
def homepage():
    """Displays 'Hello HBNB!' when the route / is requested"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    AirBnB.run(host='0.0.0.0', port=5000)
