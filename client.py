import json
import socket
import struct
import sys
from time import sleep

# chamada do programa./client IP:port Opt

IP_PORT = sys.argv[1]
OPT = sys.argv[2]

ip_port_tuple = IP_PORT.split(':')
server_IP = ip_port_tuple[0]
server_PORT = ip_port_tuple[1]
dest = (server_IP, int(server_PORT))


def open_conn_socket():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # SO_linger para resetar o socket on close
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
    tcp.connect(dest)

    return tcp


def analise0(lan, ix):
    resultados = {}

    # ix_json = json.loads(ix)
    #print(type(lan_json), len(lan_json))


    return resultados


def analise1(lan, ix, net):
    return None


def get_ix(tcp):
    response_ix = []

    tcp.send(("GET /api/ix HTTP/1.1\r\n\r\n").encode("utf-8"))
    while True:
        r_ix = tcp.recv(1024).decode("utf-8").split('\r\n\r\n')
        response_ix.append(r_ix)
        if r_ix == ['']:
            return response_ix



def get_netixlan(tcp):
    response_lan = []

    tcp.send(("GET /api/netixlan HTTP/1.1\r\n\r\n").encode("utf-8"))
    while True:
        r_lan = tcp.recv(1024).decode("utf-8").split('\r\n\r\n')
        response_lan.append(r_lan)

        if r_lan == ['']:
            return response_lan


def get_net(tcp):
    response_net = []

    tcp.send(("GET /api/net HTTP/1.1\r\n\r\n").encode("utf-8"))
    while True:
        r_net = tcp.recv(1024).decode("utf-8").split('\r\n\r\n')
        response_net.append(r_net)

        if r_net == ['']:
            return response_net


if OPT == '0':
    tcp = open_conn_socket()
    ix = get_ix(tcp)
    tcp.close()

    tcp = open_conn_socket()
    lan = get_netixlan(tcp)
    tcp.close()

    r = analise0(lan, ix)


if OPT == '1':
    tcp = open_conn_socket()
    lan = get_netixlan(tcp)
    tcp.close()

    tcp = open_conn_socket()
    ix = get_ix(tcp)
    tcp.close()

    tcp = open_conn_socket()
    net = get_net(tcp)
    tcp.close()
    analise1(lan, ix, net)


