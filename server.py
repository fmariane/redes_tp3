import json
import socket
import threading
import sys
from flask import Flask, jsonify


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


# ========== TCP ROUTINES
def tcp_handler():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    HOST = ''                 # host sera a maquina que iniciar a aplicacao
    PORT = int( sys.argv[1] ) # Porta que o servidor TCP deve ficar
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    while True:
        client_connection, address = tcp.accept()

# ========== FLASK ROUTINES
def load_json(file):
    with open(file, "r") as jsonfile:
        datastring = json.load(jsonfile)  # json to dict
        datastring = json.dumps(datastring)  # dump string
    return datastring


# endpoint /api/ix
@mypeeringdb.route('/api/ix')
def return_ix():
    ixfile = load_json(parameters["IXFILE"])
    return ixfile


# endpoint /api/ixnets/{ix_id}
@mypeeringdb.route('/api/ixnets/<int:ixid>')
def return_nets(ixid):
    json_dict = {}
    ix_nets = {}
    with open(parameters["NETIXLANFILE"], "r") as f:
        json_dict = json.load(f)["data"]

    for x in json_dict:  # cada x eh um dict

        ix_id = x["ix_id"]
        net_id = x["id"]

        try:
            ix_nets[ix_id].append(net_id)
        except KeyError:
            ix_nets[ix_id] = []

    responsedata = {'data':ix_nets[ixid]}
    return jsonify(responsedata)


@mypeeringdb.route('/api/netname/<int:netid>')
def return_net_name(netid):
    json_dict = {}
    ix_nets = {}
    with open(parameters["NETFILE"], "r") as f:
        json_dict = json.load(f)["data"]

    for x in json_dict:  # cada x eh um dict

        net_id = x["id"]
        net_name = x["name"]

        try:
            ix_nets[net_id] = net_name
        except KeyError:
            sys.stderr.write("ERRO AO INSERIR CHAVE")

    responsedata = {'data':ix_nets[netid]}
    return jsonify(responsedata)


t = threading.Thread(target=tcp_handler)  # starta primeiro o servidor tcp
t.daemon = True
t.start()
mypeeringdb.run(host='0.0.0.0', port=None, debug=None)  # servidor flask usa outra interface disponivel
