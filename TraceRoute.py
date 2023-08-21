# The purpose of this program:
# Checks if ICMP is enabled or disabled
# Conducts a traceroute from device to target IP
# Retrieve city / state
# Retrieve latitude / longitude
# Checks the time it took for the program to run

import socket
import sys
import time
from scapy.all import *
from scapy.layers.inet import IP, UDP
from ip2geotools.databases.noncommercial import DbIpCity


# This function checks if ICMP is enabled.
def icmp_enabled():
    # Try to get the hostname of localhost.
    try:
        socket.gethostbyname('localhost')
        return True
    # If the hostname cannot be resolved, ICMP is disabled.
    except socket.gaierror:
        return False


# This function performs a traceroute to the specified IP address.
def traceroute(ip_address):
    # Print the header of the traceroute.
    print(f"Traceroute to {ip_address}:")

    # For each hop, send an ICMP echo request packet with a TTL of 1 to 30.
    for i in range(1, 30):
        # Create an ICMP echo request packet with a TTL of i.
        pkt = IP(dst=ip_address, ttl=i) / UDP(dport=33434)

        # Send the packet and wait for a response for 2 seconds.
        reply = sr1(pkt, verbose=0, timeout=2)

        # If there is no response, print "No response."
        if reply is None:
            print(f"{i}: No response")

        # If the response is an ICMP echo reply, print the hop number and the source IP address.
        elif reply.type == 3:
            print(f"{i}: {reply.src}")

            # Retrieve the geolocation of the Ip address.
            geolocation = DbIpCity.get(reply.src)

            print(f"\n{reply.src}: {geolocation.city}, {geolocation.country}, "
                  f"\n(Lat: {geolocation.latitude}, Lng: {geolocation.longitude})")
            break

        # Otherwise, print the hop number and the source IP address.
        else:
            print(f"{i}: {reply.src}")


# This function calculates the execution time of the specified function.
def calculate_execution_time(func):
    # Get the start time.
    start_time = time.time()

    # Run the function.
    func()

    # Get the end time.
    end_time = time.time()

    # Return the execution time.
    return end_time - start_time


# This function is a simple function that just increments a variable a million times.
def my_function():
    for i in range(1000000):
        i += 1


# The main function.
if __name__ == "__main__":
    # Check if ICMP is enabled.
    if icmp_enabled():
        print('ICMP enabled')
    else:
        print('ICMP disabled')

    # Set the target IP address.
    target_ip = "8.8.8.8"

    # Perform a traceroute to the target IP address.
    traceroute(target_ip)

    # Calculate the execution time of the my_function function.
    execution_time = calculate_execution_time(my_function)

    # Print the execution time.
    print('\nThe execution time of the function is {} seconds.'.format(execution_time))
