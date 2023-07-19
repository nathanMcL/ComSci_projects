# To communicate with the Socket_Test remote server
# With remote server Client needs server IP address
# Send / Recieve message...eventually 

import socket

# create a socket at client side
# using TCP / IP protocol
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# connect it to server and port
# number on a local computer.
client.connect(('localhost', 9999))

# Client enters name
name = input("Enter your Name")
# Client name is sent
client.send(bytes(name, 'utf-8'))

print(client.recv(1024).decode())
