#!/usr/bin/python3
"""
This is a simple Flask web application.
It listens on 0.0.0.0:5000 and has a route that displays "Hello HBNB!".
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" when visiting the root URL."""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
