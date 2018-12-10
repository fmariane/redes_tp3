import json
import sys
import requests
from flask import Flask


def parameterHandler():
    parameter = {
        "my_PORT": sys.argv[1],
        "NETFILE": sys.argv[2],
        "IXFILE": sys.argv[3],
        "NETIXLANFILE": sys.argv[4],
    }
    return parameter


parameters = parameterHandler()


mypeeringdb = Flask(__name__)


def load_json(file):
    with open(file, "r") as jsonfile:
        datastring = json.load(jsonfile)  # json to dict
        datastring = json.dumps(datastring)  # dump string
    return datastring


# netfile = json.load(parameters["NETFILE"])
# netixlanfile = json.load(parameters["NETIXLANFILE"])

# endpoint /api/ix
@mypeeringdb.route('/api/ix')
def return_ix():
    ixfile = load_json(parameters["IXFILE"])
    return ixfile


# print('ESTE É O RETORO ix', return_ix())


@mypeeringdb.route('/api/ixnets/<int:ix_id>')
def return_net(ix_id):

    # real_peeringdb_url = 'https://www.peeringdb.com/api/net/'+str(ix_id)
    # ixnetsbyid = requests.get(url=real_peeringdb_url).json()
    # return json.dumps(ixnetsbyid, indent=4)


# print('ESTE E O RETORNO NET', json.dumps(return_net(3), indent=4))

PORT = int(parameters["my_PORT"])
mypeeringdb.run(host='0.0.0.0', port=PORT, debug=True)
