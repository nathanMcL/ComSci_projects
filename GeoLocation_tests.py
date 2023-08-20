# The Purpose of this program:
# With an Ip Address;
# Retrieve location: City/State/Country
# Retrieve grid coordinates
# Prompt for server Ip or previous used ip (see #Target Ip)
# Prompt for your Latitude
# Prompt for your Longitude
# Calculates distance between the two Ip addresses

# Import necessary modules
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

# Target IP address
ip_add = "96.120.100.1"

# Function to print the details of an IP address
def printdetails(ip):
    """
    Print the IP address, location, and grid coordinates of the specified IP address.

    Args:
        ip (str): The IP address to query.
    """
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


# Print the details of the target IP address
printdetails(ip_add)

# Function to get the distance between two IP addresses
def get_distance_from_location(ip, lat, lon):
    """
    Get the distance between the specified IP address and the specified location.

    Args:
        ip (str): The IP address to query.
        lat (float): The latitude of the location.
        lon (float): The longitude of the location.

    Returns:
        float: The distance between the IP address and the location in miles.
    """
    res = DbIpCity.get(ip)
    ip_lat, ip_lon = res.latitude, res.longitude
    return distance((ip_lat, ip_lon), (lat, lon)).mi


# Prompt for the server IP address
server_ip = input("Server's IP: ")

# Prompt for the user's latitude
lat = float(input("Your Latitude: "))

# Prompt for the user's longitude
lon = float(input("Your Longitude: "))

# Get the distance between the server and the user
dist = get_distance_from_location(server_ip, lat, lon)

# Print the distance
print(f"Distance between the server and your location is {str(dist)}mi")
