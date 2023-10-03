# Python UDP Client 
from socket import *
import sys

server_address = sys.argv[1]
n_port = int(sys.argv[2])
req_code = sys.argv[3]
messages = [sys.argv[i] for i in range(4, len(sys.argv))] + ["EXIT"]


def tcp_negotiation(server_address, n_port, req_code):
    # Python TCP Client
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # `server_address` can simply be the name of the server
    clientSocket.connect((server_address, n_port))
    try: 
        clientSocket.send(req_code.encode())
        r_port = int(clientSocket.recv(1024).decode())
    except:
        print('The connection is closed by the server')
        clientSocket.close()
        return 0, 1 
    clientSocket.close()
    return int(r_port), 0


def udp_transaction(server_address, r_port):
    # create UDP packet
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    output = []
    for string in messages:
        # python will do the DNS query under the hood 
        # so we only specify serverName instead of IP address here
        clientSocket.sendto(string.encode(), (server_address, r_port))
        if string == 'EXIT':
            print(", ".join(output))
            break
        # read reply data (bytes from socket)
        response, serverAddress = clientSocket.recvfrom(2048)
        if response.decode() == 'LIMIT':
            print(", ".join(output) + ",", "Request limit reached")
            break
        else: 
            output.append(response.decode())
    clientSocket.close()


r_port, statues_code = tcp_negotiation(server_address, n_port, req_code)
if not statues_code:
    print(f"r_port={r_port}")
    udp_transaction(server_address, r_port)
