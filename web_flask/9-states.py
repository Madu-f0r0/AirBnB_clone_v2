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


@app.route("/states", strict_slashes=False)
def states():
    """Displays the list of states"""
    all_states = storage.all("State").values()
    return render_template("9-states.html", all_states=all_states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays dynamic HTML page for URI `/states/<id>`"""
    all_states = storage.all("State").values()
    for state in all_states:
        if id == state.id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
