from flask import Flask
import requests

peeringdb = Flask(__name__)


@peeringdb.route('/')
def get_exchange_points():
    # endpoint /api/ix
    return "exchange point"


def exchangePointByID():
    return "exchange point by id"


peeringdb.run(debug=True)
