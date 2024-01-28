#!/usr/bin/python3
"""Starting a Flask web application.

Application listens on 0.0.0.0, port 5000.
Routes:
    /: Displaying 'Hello HBNB!'.
    /hbnb: Displaying 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")