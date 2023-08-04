# The Purpose of this program is to:
# Retrieve the Operating system information,
# Retrieve the Mac Address,
# Monitor the selected port's connection,
# Retrieve the Ip Address of the port,
# Retrieve the Wi-Fi network information,
# Retrieve the battery percentage, detect if the device is plugged in,
# Retrieve the Network mask/sub-mask IPs
# Retrieve the all the Hosts under this network
# Retrieve if the Network overlaps another Network
# Retrieve GEO-location- (I don't like how the returned data is all on one line)

# Has redundant ran information in separate locations,
# Example: The Battery information

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

import psutil
import serial.tools.list_ports
from BatteryUsage import convertTime
from SystemInformation import ping


def get_system_info():
    """Retrieves the system information."""
    system = platform.uname()
    return {
        "system": system.system,
        "node": system.node,
        "release": system.release,
        "version": system.version,
        "machine": system.machine,
        "processor": system.processor,
    }


def get_mac_address():
    """Retrieves the MAC address."""
    return ":".join(re.findall("..", "%012x" % uuid.getnode()))


def get_network_info():
    """Retrieves the network information."""
    network = ipaddress.IPv4Network("000.000.0.0")
    ip_address = ipaddress.ip_address("000.000.0.0")

    return {
        "network_mask": network.netmask,
        "broadcast_address": network.broadcast_address,
        "num_addresses": network.num_addresses,
        "subnets": network.subnets(prefixlen_diff=2),
        "is_global": ip_address.is_global,
        "is_link_local": ip_address.is_link_local,
    }


def get_battery_info():
    """Retrieves the battery information."""
    battery = psutil.sensors_battery()
    return {
        "percent": battery.percent,
        "power_plugged": battery.power_plugged,
        "secsleft": battery.secsleft,
    }


def get_ram_info():
    """Retrieves the RAM information."""
    return {
        "used_gb": psutil.virtual_memory()[2] / 1024 ** 3,
        "used_percent": psutil.virtual_memory()[3],
    }


def get_network_status():
    """Retrieves the network status."""
    if ping():
        return "connected"
    else:
        return "disconnected"


def main():
    """Runs the main program."""
    system_info = get_system_info()
    mac_address = get_mac_address()
    network_info = get_network_info()
    battery_info = get_battery_info()
    ram_info = get_ram_info()
    network_status = get_network_status()

    print("System information:")
    print(system_info)
    print()
    print("MAC address:")
    print(mac_address)
    print()
    print("Network information:")
    print(network_info)
    print()
    print("Battery information:")
    print(battery_info)
    print()
    print("RAM information:")
    print(ram_info)
    print()
    print("Network status:")
    print(network_status)


def date_time():
    """Prints the date and 24-hour time."""
    now = datetime.datetime.now()
    print(f"Date: {now.strftime('%Y-%m-%d')}")
    print(f"Time: {now.strftime('%H:%M:%S')}")


if __name__ == "__main__":
    main()
