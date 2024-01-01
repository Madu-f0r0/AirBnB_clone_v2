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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays dynamic HTML page for URI `/cities_by_states`"""
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
