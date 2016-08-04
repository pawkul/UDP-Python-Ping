# Import socket module
from socket import *
import sys
# Import time modules    
import datetime
import time

# Create an UDP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_DGRAM is used for UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get the ip address and the port number
name_machine = getfqdn()
ip = gethostbyname(name_machine)
port = 12000
address = ('127.0.0.1', port)

# Time out 1 second for the response from the server
clientSocket.settimeout(1)

for e in range(1,11):
    # Ping message
    data = 'data'
    # Time when packet is sent
    time_at = time.time()
    # Send the ping
    clientSocket.sendto(data.encode(), address)
    try:
        # Try receiving a response
        clientSocket.recvfrom(1024)
        # Time when response is received
        time_after = time.time()
        # Print packet number and round trip time
        print("Ping", str(e), str(round(time_after - time_at, 5)))

    except timeout:
        # Packet lost
        print("Request timed out")
