#!/usr/bin/python3
"""
AirBnB Clone
*** Web Framework with Flask ***
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Start Flask """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_start():
    """ Start hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ Use of string variable """
    modified_text = text.replace("_", " ")
    return f"C {modified_text}"


if __name__ == "__main__":
    # python3 -m web_flask.2-c_route
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
