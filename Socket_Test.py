# To communicate with client input client IP address
# Greet the client
# Request status from client
# Prompt follow-up question from a client

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
print()

while True:
    client, address = server.accept()
    name = client.recv(1024).decode()
    print("Connected with", address, name)

    # Greeting to a client
    client.send(bytes('Welcome, I am MacN, Your Admin', 'utf-8'))
    print()
    # Prompt client for a status respond
    client.send(bytes('What is your status?', 'utf-8'))
    # Prompt client with sending error message or follow-up question / response
    client.send(bytes('What is your issue/error?', 'utf-8'))

    # Client Status Message
    msg = client.recv(1024)
    while msg:
        print('Received Status:' + msg.decode())
        msg = client.recv(1024)

    print()
    # Client error message or follow-up question / response
    msg_two = b''
    while not msg_two.endswith(b'\n'):
        msg_two = client.recv(1024)
    print('Send error or follow-up question.' + msg_two.decode())

    client.close()
