# The purpose of this program is to scan for open ports and return which are open, with banner


import socket
import threading
import time

# Scan for open ports
def scan_port(port):
    try:
        host = "localhost"
        host_ip = socket.gethostbyname(host)
        status = False

        # instance of a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connecting the host ip address and port
        s.connect((host_ip, port))
        try:
            banner = s.recv(1024).decode()
            print("port {} is open with banner {}".format(port, banner))
        except:
            print("port {} is open ".format(port))

    except:
        pass

start_time = time.time()

for i in range(0, 100000):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()

end_time = time.time()
print("To scan all ports it took {} seconds".format(end_time-start_time))