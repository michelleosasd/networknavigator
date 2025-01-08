import os
import subprocess
import platform
import socket

class NetworkNavigator:
    def __init__(self):
        self.os_type = platform.system()

    def ping(self, host='8.8.8.8'):
        """ Ping a host to check connectivity """
        try:
            # Different ping command for Windows
            command = ['ping', '-n', '4', host] if self.os_type == 'Windows' else ['ping', '-c', '4', host]
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            print(f"Ping results for {host}:\n{output}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to ping {host}. Error: {e.output}")

    def trace_route(self, host='8.8.8.8'):
        """ Trace route to host to check path taken by packets """
        try:
            # Different traceroute command for Windows
            command = ['tracert', host] if self.os_type == 'Windows' else ['traceroute', host]
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            print(f"Trace route results for {host}:\n{output}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to trace route to {host}. Error: {e.output}")

    def display_ip_config(self):
        """ Display network configuration details """
        try:
            # Using ipconfig for Windows
            command = ['ipconfig'] if self.os_type == 'Windows' else ['ifconfig']
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            print(f"Network configuration:\n{output}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to get network configuration. Error: {e.output}")

    def get_host_name_ip(self):
        """ Get the host name and IP address """
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print(f"Host Name: {host_name}")
            print(f"Host IP: {host_ip}")
        except Exception as e:
            print(f"Unable to get Hostname and IP: {e}")

if __name__ == '__main__':
    navigator = NetworkNavigator()
    print("Network Navigator - Enhancing your network exploration experience")
    
    print("\n1. Ping a host")
    navigator.ping()

    print("\n2. Trace route to a host")
    navigator.trace_route()

    print("\n3. Display IP configuration")
    navigator.display_ip_config()

    print("\n4. Get Host Name and IP")
    navigator.get_host_name_ip()