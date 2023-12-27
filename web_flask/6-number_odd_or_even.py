#!/usr/bin/python3
""" This module starts a basic web app.

Listening port: 5000
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Display when no URI is specified"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display `HBNB` for URI `/hbnb`"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
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
    """Displays the text for `/number/n`"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an html page if `n` is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays a dynamic html page if `n` is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)
