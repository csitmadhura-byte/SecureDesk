import sys
import os

# Add the main project folder to Python's module search path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)


from modules.system_info import get_system_info
from modules.network_check import get_network_info
from modules.process_monitor import get_top_processes
from modules.disk_health import get_disk_health
from modules.event_analyzer import analyze_security_events
from modules.firewall_check import get_firewall_status


def test_system_info():

    data = get_system_info()

    assert isinstance(data, dict)
    assert "hostname" in data
    assert "cpu_usage" in data
    assert "memory_usage" in data
    assert "disk_usage" in data

    print("PASS: System Information")


def test_network_info():

    data = get_network_info()

    assert isinstance(data, dict)
    assert "hostname" in data
    assert "local_ip" in data
    assert "internet" in data
    assert "dns" in data

    print("PASS: Network Diagnostics")


def test_process_monitor():

    processes = get_top_processes()

    assert isinstance(processes, list)

    print("PASS: Process Monitor")


def test_disk_health():

    data = get_disk_health()

    assert isinstance(data, dict)
    assert "total_gb" in data
    assert "free_gb" in data
    assert "usage_percent" in data
    assert "status" in data

    print("PASS: Disk Health")


def test_security_events():

    data = analyze_security_events()

    assert isinstance(data, dict)
    assert "successful_logins" in data
    assert "failed_logins" in data
    assert "threshold" in data
    assert "status" in data

    print("PASS: Security Events")


def test_firewall():

    data = get_firewall_status()

    assert isinstance(data, dict)
    assert "status" in data
    assert "profiles" in data

    print("PASS: Firewall Check")


if __name__ == "__main__":

    print("=" * 55)
    print("       SECUREDESK MODULE TESTING")
    print("=" * 55)

    test_system_info()
    test_network_info()
    test_process_monitor()
    test_disk_health()
    test_security_events()
    test_firewall()

    print("\n" + "=" * 55)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 55)