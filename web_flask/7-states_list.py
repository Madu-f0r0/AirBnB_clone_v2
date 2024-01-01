#!/usr/bin/python3
""" This module is a basic web app on Flask

Listening port: 5000
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exc):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays dynamic HTML page for URI `/states_list`"""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(debug=True)
