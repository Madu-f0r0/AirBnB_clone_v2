#!/usr/bin/python3
""" This module starts a basic web app.

Listening port: 5000
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Display when no URI is specified"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display `HBNB` for URI `/hbnb`"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display variable text for `/c/<text>`"""

    sub_strings = text.split('_')
    return "C " + " ".join(sub_strings)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """Display variable text for `/python/<text>`"""

    sub_strings = text.split("_")
    return "Python " + " ".join(sub_strings)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True)
