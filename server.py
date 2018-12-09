from flask import Flask
import json
import requests
import sys

def parameterHandler():
    parameter = {
        "my_PORT": sys.argv[1],
        "NETFILE": sys.argv[2],
        "IXFILE": sys.argv[3],
        "NETIXLANFILE": sys.argv[4],
    }
    return parameter

mypeeringdb = Flask(__name__)

# GET que recupera todos IXs ================================
def get_ix():
    req = requests.get('https://www.peeringdb.com/api/ix')
    req_json = req.json()
    return req_json


def get_ix_nets():
    req = requests.get('https://www.peeringdb.com/api/net')
    req_json = req.json()
    return req_json

def get_ix_netlan():
    req = requests.get('https://www.peeringdb.com/api/netixlan')
    req_json = req.json()
    return req_json
# ===========================================================
parameters = parameterHandler()

def load_json(file):
    with open(file, "r") as jsonfile:
        datastring = json.load(jsonfile)
        datastring = json.dumps(datastring)
    return datastring


#netfile = json.load(parameters["NETFILE"])
#netixlanfile = json.load(parameters["NETIXLANFILE"])

#endpoint /api/ix
@mypeeringdb.route('/api/ix')
def return_ix():
    ixfile = load_json(parameters["IXFILE"])
    return ixfile

def return_net

mypeeringdb.run(debug=True)
