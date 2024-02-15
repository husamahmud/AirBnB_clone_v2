#!/usr/bin/python3
from flask import Flask

AirBnB = Flask(__name__)


@AirBnB.route('/')
def homepage():
    return 'Hello HBNB!'


if __name__ == '__main__':
    AirBnB.run(debug=True,
               port=5000)
