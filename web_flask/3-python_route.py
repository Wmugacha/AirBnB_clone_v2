#!/usr/bin/python3
"""
AirBnB Clone
*** Web Framework with Flask ***
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function to display Hello hbnb """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_start():
    """ Function to display hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ Function to display C with a value variable """
    return 'C ' + text.replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text="is cool"):
    """ Function to display Python with a value variable """
    return 'Python ' + text.replace("_", " ")


if __name__ == "__main__":
    # python3 -m web_flask.2-c_route
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
