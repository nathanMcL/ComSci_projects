# The Purpose of this program is to:
# Retrieve the Operating system information, 
# Retrieve the Mac Address, 
# Monitor the selected port's connection, 
# Retrieve the Ip Address of the port, 
# Retrieve the Wi-Fi network information, 
# Retrieve the battery percentage, detect if the device is plugged in
# Retrieve the Network mask/sub-mask IPs
# Retrieve all the Hosts under this network
# Retrieve if the Network overlaps another Network
# Retrieve GEO-location- (I don't like how the returned data is all on one line)

import ipaddress
import os
import sys
import socket
import datetime
import time
import platform
import re, uuid
from ipaddress import ip_address
import subprocess
import serial.tools.list_ports
# Battery Usage
import psutil
import json
import requests

from BatteryUsage import convertTime

my_system = platform.uname()
# Battery Usage (returns a tuple)
battery = psutil.sensors_battery()
# Initialize an IPv4 address
IP = ipaddress.IPv4Address("000.000.00.00")
# Initialize an IPv4 Network
network = ipaddress.IPv4Network("000.000.1.0/00")
# IP address to track
IP_Address = 'localhost'

# Retrieve the CPU System information
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
print()

# Retrieve the Mac Address
print("The Mac Address formatted : ", end="")
print(':'.join(re.findall('..', '%012x' % uuid.getnode())))
# Retrieve network Mask
print("Network mask: ", network.netmask)
print()

# Track IP Address Location
request_url = 'https://geolocation-db.com/jsonp/' \
              + IP_Address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
print("IP Address Location","\n", result)

# Retrieve the IP Address at selected port
print(f"IP Address: {ip_address}")
# Retrieve the Broadcast Address
print("Broadcast Address: ", network.broadcast_address)
# Retrieve the number of IP addresses under this network
print("Number of hosts under", str(network), ":", network.num_addresses)
# Retrieve the Subnets of this network
print("Subnets: ")
for subnet in network.subnets(prefixlen_diff=2):
    print(subnet)
print()

# Check if supplied IP Address is a global or local address
# True if Global
print("Is global:", IP.is_global)
# True if Local
print("Is link-local:", IP.is_link_local)

# Retrieve the Internet Network Information
# Using the check_output() for having the network terminal retrieval
devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
# decode it to strings
devices = devices.decode('ascii')
devices = devices.replace("\r", "")
# displaying the information
print(devices)

FILE = os.path.join(os.getcwd(), "networkinfo.log")

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

print()

# Battery Usage
print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)
# Converting seconds to hh:mm:ss
print("Battery left : ", convertTime(int(battery.secsleft)))

print()
# Getting % usage of the Virtual Memory
print('RAM Used (GB):', psutil.virtual_memory()[2])
# Getting usage of Virtual Memory in GB
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)

print()

#Detects if this network overlaps another network
print("Overlaps 000.000.1.0/24", network.overlaps(ipaddress.IPv4Network("000.000.1.0/24")))

# creating log file in the current directory
# ??getcwd?? get current directory,
# os function, ??path?? to specify a path

# Ping
def ping():
    # Ping a particular IP
    try:
        # if no connection timeout after 3 seconds.
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_NET: address family
        # SOCK_STREAM: type for TCP

        host = "localhost"
        port = 23132

        server_address = (host, port)
        s.connect(server_address)

    # function returns false value
    # after data interruption
    except OSError as error:
        return False

    else:
        # closing the connection after the
        # communication with the server is completed
        s.close()
        return True


# Calculate Time
def calculate_time(start, stop):
    # calculating unavailability
    # time and converting it into seconds
    difference = stop - start
    seconds = float(str(difference.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]


# First Check
# To check if the system was already
# connected to an internet connection
def first_check():
    # if ping returns true
    if ping():
        live = "\nCONNECTION ACQUIRED\n"
        print(live)
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "connection acquired at: " + \
                            str(connection_acquired_time).split(".")[0]
        print(acquiring_message)
        # writes into the log file
        with open(FILE, "a") as file:
            file.write(live)
            file.write(acquiring_message)
        return True

    else:
        # if the ping returns false
        not_live = "\nCONNECTION NOT ACQUIRED\n"
        print(not_live)

        with open(FILE, "a") as file:
            # writes into the log file
            file.write(not_live)
        return False


# Main
def main():
    # main function to call functions
    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = "monitoring started at: " + \
                           str(monitor_start_time).split(".")[0]

    if first_check():
        # if true
        print(monitoring_date_time)
        # monitoring will only start when
        # the connection will be acquired

    else:
        # if false
        while True:
            # infinite loop to see if the connection is acquired
            if not ping():
                # if connection isn't acquired
                time.sleep(1)
            else:
                # if connection is acquired
                first_check()
                print(monitoring_date_time)
                break
    # write into the file as a into networkinfo.log,
    # "a" - append: opens file for appending,
    # creates the file if it does not exist???
    with open(FILE, "a") as file:
        file.write("\n")
        file.write(monitoring_date_time + "\n")

    while True:
        # infinite loop, as we are monitoring
        # the network connection till the machine runs
        if ping():
            # if true: the loop will execute after every 5 seconds
            time.sleep(5)

        else:
            # if false: a fail message will be displayed
            down_time = datetime.datetime.now()
            fail_msg = "disconnected at: " + str(down_time).split(".")[0]
            print(fail_msg)

            with open(FILE, "a") as file:
                # writes inti the log file
                file.write(fail_msg + "\n")

            # Infinite loop will run till ping() return true
            while not ping():
                time.sleep(1)
            up_time = datetime.datetime.now()

            # after loop breaks, connection restored
            uptime_message = "connected again: " + str(up_time).split(".")[0]

            down_time = calculate_time(down_time, up_time)
            unavailability_time = "connection was unavailable for: " + down_time

            print(uptime_message)
            print(unavailability_time)

            with open(FILE, "a") as file:

                # log entry for connection restoration time,
                # and unavailability time
                file.write(uptime_message + "\n")
                file.write(unavailability_time + "\n")

#print()
# iterate over all the hosts under this network
#print("Hosts under", str(network), ":")
#for host in network.hosts():
#    print(host)


main()
