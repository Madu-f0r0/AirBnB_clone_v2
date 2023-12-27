#!/usr/bin/python3
""" This module starts a basic web app.

Listening port: 5000
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Display when no URI is specified"""

    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True)
