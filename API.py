# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#implementing-our-api
import flask
import json
from flask import request, jsonify
import mysql.connector
import configparser
import sys
import time


app = flask.Flask(__name__)

# API

@app.route('/api/telemetrie', methods=['GET'])
def telemetrie():
    results = {}
    results['Telemetrie'] = "Telemetrie"
    return results

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run(host='0.0.0.0', debug=True, port=5000)
