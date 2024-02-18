#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

AirBnB = Flask(__name__)


@AirBnB.route('/', strict_slashes=False)
def homepage():
    """Displays 'Hello HBNB!' when the route / is requested"""
    return 'Hello HBNB!'


@AirBnB.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when the route /hbnb is requested"""
    return 'HBNB'


@AirBnB.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    AirBnB.run(host='0.0.0.0', port=5000)
