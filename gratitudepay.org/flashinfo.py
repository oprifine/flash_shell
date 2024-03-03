import psutil
import socket
import platform

def get_network_connections():
    try:
        # Get the list of network connections
        connections = psutil.net_connections(kind='inet')
        return connections
    except Exception as e:
        print(f"Error fetching network connections: {e}")
        return []

def get_local_socket_info():
    try:
        # Get local socket information
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name, host_ip
    except Exception as e:
        print(f"Error fetching local socket information: {e}")
        return "", ""

def custom_netstat():
    # Get network connections
    connections = get_network_connections()

    # Get local socket information
    host_name, host_ip = get_local_socket_info()

    # Get platform information
    platform_info = platform.platform()

    # Print header
    print("Custom-netstat - Device Information:")
    print(f"Platform: {platform_info}")
    print(f"Local Host: {host_name} ({host_ip})\n")

    print("Network Connections:")
    print("Proto\tLocal Address\t\tForeign Address\t\tStatus")

    # Print network connections
    for conn in connections:
        print(f"{conn.type}\t{conn.laddr}\t\t{conn.raddr}\t\t{conn.status}")

if __name__ == "__main__":
    print("Welcome to custom-netstat!")
    print("Running custom-netstat...")

    custom_netstat()

    print("\nCustom-netstat has completed.")
