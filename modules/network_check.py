import socket
import subprocess


def get_network_info():
    info = {}

    # Get hostname
    hostname = socket.gethostname()
    info["hostname"] = hostname

    # Get local IP address
    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        local_ip = "Unable to determine"

    info["local_ip"] = local_ip

    # Test internet connectivity
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            info["internet"] = "PASS"
        else:
            info["internet"] = "FAIL"

    except Exception:
        info["internet"] = "ERROR"

    # Test DNS resolution
    try:
        socket.gethostbyname("google.com")
        info["dns"] = "PASS"
    except socket.error:
        info["dns"] = "FAIL"

    return info


if __name__ == "__main__":
    data = get_network_info()

    print("\n===== NETWORK DIAGNOSTICS =====")
    print("Hostname:", data["hostname"])
    print("Local IP:", data["local_ip"])
    print("Internet Connectivity:", data["internet"])
    print("DNS Resolution:", data["dns"])