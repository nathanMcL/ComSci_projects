# With remote server Client needs server IP address

import socket

client = socket.socket()

client.connect(('localhost', 9999))

name = input("Enter your Name")
client.send(bytes(name, 'utf-8'))

print(client.recv(1024).decode())
