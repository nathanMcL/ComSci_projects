# The purpose of this program is to communicate with a client
# To communicate with client input client IP address
# Send a message to a client...eventually
import socket

# Create a socket at server side
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
print('Socket Created')

# Bind the socket with server
# and port number
server.bind(('localhost', 9999))

# Allow maximum connection: 3
# to the socket
server.listen(3)
print('waiting for connections')

while True:
    client, address = server.accept()
    name = client.recv(1024).decode()
    print("Connected with", address, name)

    client.send(bytes('Welcome, I am MacN, Your Admin', 'utf-8'))

    # Send a message to a client
    #client.send(b"what is your status?")
    #msg = "Status check"
    #client.send(msg.encode())

    client.close()
