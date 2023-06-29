# Hello and what have you,

import socket

# Send Message
def send_message(host, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall((message.encode("utf-8")))
    sock.close()

if __name__ == "__main__":
    host = "localhost"
    port = 23130
    message = "Hello World! Drink water, to beat the heat!!"
    send_message(host, port, message)
