import json
import socket
import struct
import sys

# chamada do programa./client IP:port Opt

IP_PORT = sys.argv[1]
OPT = sys.argv[2]

ip_port_tuple = IP_PORT.split(':')
server_IP = ip_port_tuple[0]
server_PORT = ip_port_tuple[1]
dest = (server_IP, int(server_PORT))

try:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.connect(dest)
    except socket.error:
        print("erro connect tcp")
        # sys.stderr.write("erro connect tcp")

except socket.error:
    print("erro criacao do socket")
    # sys.stderr.write("erro criacao do socket")


def analytics(IX, NET, NETIXLAN):
    IX = NET = NETIXLAN = ''
    return 'results'


resposta = tcp.recv(2048)
