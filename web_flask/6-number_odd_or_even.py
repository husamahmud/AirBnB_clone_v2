#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

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


@AirBnB.route('/python/', strict_slashes=False)
@AirBnB.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Displays 'Python' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@AirBnB.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@AirBnB.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@AirBnB.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if n is an integer"""
    if n % 2 == 0:
        return render_template('5-number.html', n=f'{n} is even')
    return render_template('5-number.html', n=f'{n} is odd')


if __name__ == '__main__':
    AirBnB.run(host='0.0.0.0', port=5000)
