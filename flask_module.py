#!/usr/bin/env python3

"""
Flask is a Python pkg or web framework for creating websites
on Ubuntu and Unix.
eg. 'sudo pip install Flask==0.11.1' will install Flask with a
particular version. Without the (==) and version number, the
latest version will be downloaded and installed.
Visit http://flask.pocoo.org/docs/1.0/ to learn more about how
this works.
"""

# Importing the Flask module from the flask pkg.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

app.run(port=8080)
