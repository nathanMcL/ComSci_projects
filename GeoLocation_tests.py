# The Purpose of this program:
# With an Ip Address;
# Retrieve location: City/State/Country
# Retrieve grid coordinates
# Prompt for server Ip or previous used ip (see #Target Ip)
# Prompt for your Latitude
# Prompt for your Longitude
# Calculates distance between the two Ip addresses

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

# Target Ip
ip_add = "96.120.100.1"


def printdetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


printdetails(ip_add)


def get_distance_from_location(ip, lat, lon):
    res = DbIpCity.get(ip)
    ip_lat, ip_lon = res.latitude, res.longitude
    return distance((ip_lat, ip_lon), (lat, lon)).mi


server_ip = input("Server's IP: ")
lat = float(input("Your Latitude: "))
lng = float(input("Your Longitude: "))

dist = get_distance_from_location(server_ip, lat, lng)
print(f"Distance between the server and your location is {str(dist)}mi")
