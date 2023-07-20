# To communicate with the Socket_Test remote server
# With remote server Client needs server IP address
# Client enters name
# Client enters their status
# When PROMPTED Client enters a error message or follow-up question / response

import ipaddress
import socket
import datetime

from win32timezone import now

# create a socket at client side
# using TCP / IP protocol
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# connect it to server and port
# number on a local computer.
client.connect(('localhost', 9999))
print("Connected to localhost")
print()

# Client enters name
name = input("Enter your Name")
# Client name is sent
client.send(bytes(name, 'utf-8'))

# Receive Sock_Test messages
print(client.recv(1024).decode())
print()
print(client.recv(1024).decode())
print()

# Client enters a status response
msg = input("Enter your Status:")
client.send(bytes(msg, 'utf-8'))

# When PROMPTED Client enters a error message or follow-up question / response
msg_two = input("Enter an error message or question")
client.send(bytes(msg_two, 'utf-8'))





