# Python UDP Server 
from socket import *
import random
import sys

req_code = sys.argv[1]
req_lim = int(sys.argv[2])

# TCP negotiation

serverPort = 12000
# create TCP welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)
while True:
    try:
        serverSocket.bind(("",serverPort))
        print(f"SERVER_PORT={serverPort}")
        break
    except:
        serverPort += 1

# server begins listening for incoming TCP requests
serverSocket.listen(1)

while True:
    # server waits on accept() for incoming requests
    # new socket created on return
    connectionSocket, addr = serverSocket.accept()
    # read bytes from socket (but not address as in UDP)
    request = connectionSocket.recv(1024).decode()
    print(f"req_code from client {addr} is {request}")
    if int(request) == int(req_code):
        # Generate a random port and check availability
        r_port = random.randint(1025, 65535)
        udpSocket = socket(AF_INET, SOCK_DGRAM)
        while True:
            try: 
                # bind socket to local port
                udpSocket.bind(("0.0.0.0", r_port))
                break
            except:
                r_port = random.randint(1025, 65535)
        print('New connection:')
        connectionSocket.send(str(r_port).encode())   
        print(f"r_port {r_port} is used")
    else:
        print("The client failed to send the intended req_code.")
        connectionSocket.close()
        continue
    connectionSocket.close()

    # Start UDP Transaction

    def is_palindrome(string):
        return string == string[::-1]

    # Start UDP Server for Transactions on the random port

    count = 0
    while count <= req_lim:
        # Read from UDP socket into message
        # getting client’s address (client IP and port)
        message, clientAddress = udpSocket.recvfrom(2048)
        if message.decode() == "EXIT":
            break
        if count == req_lim:
            udpSocket.sendto("LIMIT".encode(), clientAddress)
            print("Request limit reached")
            break
        elif is_palindrome(message.decode()):
            udpSocket.sendto("TRUE".encode(), clientAddress)
        else:
            udpSocket.sendto("FALSE".encode(), clientAddress)
        count += 1
        
    udpSocket.close()



