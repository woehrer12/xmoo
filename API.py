# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#implementing-our-api
import flask
from flask import request, jsonify
import GYRO

Gyro = GYRO.GYRO()

app = flask.Flask(__name__)

# API

@app.route('/api/telemetrie', methods=['GET'])
def telemetrie():
    Gyro.request()
    results = {'Telemetrie' : {"Gyro" : {}}}
    results['Telemetrie']['Gyro'] = Gyro.json()
    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run(host='0.0.0.0', debug=True, port=5000)
