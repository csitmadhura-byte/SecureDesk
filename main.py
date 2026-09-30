from modules.system_info import get_system_info
from modules.network_check import get_network_info
from modules.process_monitor import get_top_processes
from modules.disk_health import get_disk_health
from modules.event_analyzer import analyze_security_events
from modules.firewall_check import get_firewall_status

from modules.logger import (
    setup_logger,
    log_info,
    log_warning,
    log_error
)

from modules.database import (
    create_database,
    save_scan,
    get_scan_history
)

from modules.report_generator import (
    generate_html_report,
    open_report
)


def show_system_info():

    try:

        data = get_system_info()

        print("\n===== SYSTEM INFORMATION =====")

        print("Hostname:", data["hostname"])
        print("OS:", data["os"])
        print("OS Version:", data["os_version"])
        print("Architecture:", data["architecture"])
        print("Processor:", data["processor"])
        print("CPU Usage:", data["cpu_usage"], "%")
        print("Memory Usage:", data["memory_usage"], "%")
        print("Disk Usage:", data["disk_usage"], "%")

        save_scan(
            "System Information",
            "PASS",
            f"CPU: {data['cpu_usage']}%, "
            f"Memory: {data['memory_usage']}%"
        )

        log_info(
            "System information check completed."
        )

    except Exception as error:

        print(
            "\nError while collecting system information."
        )

        print("Error:", error)

        log_error(
            f"System information error: {error}"
        )


def show_network_info():

    try:

        data = get_network_info()

        print("\n===== NETWORK DIAGNOSTICS =====")

        print("Hostname:", data["hostname"])
        print("Local IP:", data["local_ip"])
        print(
            "Internet Connectivity:",
            data["internet"]
        )
        print(
            "DNS Resolution:",
            data["dns"]
        )

        status = "PASS"

        if (
            data["internet"] != "PASS"
            or data["dns"] != "PASS"
        ):

            status = "WARNING"

        save_scan(
            "Network Diagnostics",
            status,
            f"Internet: {data['internet']}, "
            f"DNS: {data['dns']}"
        )

        log_info(
            "Network diagnostics completed."
        )

    except Exception as error:

        print(
            "\nError while running network diagnostics."
        )

        print("Error:", error)

        log_error(
            f"Network diagnostics error: {error}"
        )


def show_process_info():

    try:

        processes = get_top_processes()

        print("\n===== TOP RUNNING PROCESSES =====")

        print("-" * 65)

        print(
            f"{'PID':<10}"
            f"{'Process':<30}"
            f"{'CPU %':<10}"
            f"{'Memory %':<10}"
        )

        print("-" * 65)

        for process in processes:

            print(
                f"{process['pid']:<10}"
                f"{process['name'][:28]:<30}"
                f"{process['cpu']:<10.1f}"
                f"{process['memory']:<10.1f}"
            )

        save_scan(
            "Process Monitor",
            "PASS",
            f"Monitored {len(processes)} processes."
        )

        log_info(
            "Process monitoring completed."
        )

    except Exception as error:

        print(
            "\nError while monitoring processes."
        )

        print("Error:", error)

        log_error(
            f"Process monitoring error: {error}"
        )


def show_disk_health():

    try:

        data = get_disk_health()

        print("\n===== DISK HEALTH =====")

        print(
            f"Total Space: "
            f"{data['total_gb']:.2f} GB"
        )

        print(
            f"Used Space: "
            f"{data['used_gb']:.2f} GB"
        )

        print(
            f"Free Space: "
            f"{data['free_gb']:.2f} GB"
        )

        print(
            f"Usage: "
            f"{data['usage_percent']:.1f}%"
        )

        print(
            f"Status: "
            f"{data['status']}"
        )

        print(
            f"Message: "
            f"{data['message']}"
        )

        save_scan(
            "Disk Health",
            data["status"],
            f"Disk usage: "
            f"{data['usage_percent']:.1f}%"
        )

        if data["status"] in [
            "WARNING",
            "CRITICAL"
        ]:

            log_warning(
                data["message"]
            )

        else:

            log_info(
                "Disk health check completed successfully."
            )

    except Exception as error:

        print(
            "\nError while checking disk health."
        )

        print("Error:", error)

        log_error(
            f"Disk health error: {error}"
        )


def show_security_events():

    try:

        data = analyze_security_events()

        print(
            "\n===== WINDOWS SECURITY EVENTS ====="
        )

        print(
            "Analysis Period: Last 24 hours"
        )

        print(
            "Successful Logins (4624):",
            data["successful_logins"]
        )

        print(
            "Failed Logins (4625):",
            data["failed_logins"]
        )

        print(
            "Threshold:",
            data["threshold"]
        )

        print(
            "Status:",
            data["status"]
        )

        print(
            "Message:",
            data["message"]
        )

        save_scan(
            "Windows Security Events",
            data["status"],
            f"Successful: "
            f"{data['successful_logins']}, "
            f"Failed: "
            f"{data['failed_logins']}"
        )

        if data["status"] == "WARNING":

            log_warning(
                "Multiple failed login attempts "
                f"detected: {data['failed_logins']}"
            )

        else:

            log_info(
                "Windows security event analysis "
                "completed."
            )

    except Exception as error:

        print(
            "\nError while analyzing "
            "Windows security events."
        )

        print("Error:", error)

        log_error(
            f"Security event analysis error: {error}"
        )


def show_firewall_status():

    try:

        data = get_firewall_status()

        print(
            "\n===== WINDOWS FIREWALL STATUS ====="
        )

        for profile in data["profiles"]:

            status = (
                "ENABLED"
                if profile["enabled"]
                else "DISABLED"
            )

            print(
                f"{profile['name']}: "
                f"{status}"
            )

        print(
            "\nOverall Status:",
            data["status"]
        )

        print(
            "Message:",
            data["message"]
        )

        save_scan(
            "Windows Firewall",
            data["status"],
            data["message"]
        )

        if data["status"] == "WARNING":

            log_warning(
                "One or more Windows Firewall "
                "profiles are disabled."
            )

        elif data["status"] == "ERROR":

            log_error(
                "Unable to retrieve Windows "
                "Firewall status."
            )

        else:

            log_info(
                "Windows Firewall status check "
                "completed."
            )

    except Exception as error:

        print(
            "\nError while checking "
            "Windows Firewall."
        )

        print("Error:", error)

        log_error(
            f"Firewall check error: {error}"
        )


def show_scan_history():

    try:

        records = get_scan_history(
            limit=10
        )

        print("\n")
        print("=" * 100)

        print(
            "                 SECUREDESK SCAN HISTORY"
        )

        print("=" * 100)

        print(
            "\nTotal records found:",
            len(records)
        )

        if not records:

            print(
                "\nNo scan history available."
            )

            print(
                "Run a system check first."
            )

            return

        print()

        for record in records:

            scan_id = record[0]
            scan_type = record[1]
            status = record[2]
            details = record[3]
            timestamp = record[4]

            print("-" * 100)

            print(
                f"Scan ID    : {scan_id}"
            )

            print(
                f"Scan Type  : {scan_type}"
            )

            print(
                f"Status     : {status}"
            )

            print(
                f"Details    : {details}"
            )

            print(
                f"Timestamp  : {timestamp}"
            )

        print("-" * 100)

        print(
            "\nLatest 10 scan records displayed."
        )

    except Exception as error:

        print(
            "\n===== SCAN HISTORY ERROR ====="
        )

        print(
            "Error:",
            error
        )

        log_error(
            f"Scan history error: {error}"
        )


def show_html_report():

    try:

        print(
            "\n===== GENERATING HTML REPORT ====="
        )

        print(
            "Collecting system information..."
        )

        system_data = get_system_info()

        print(
            "Collecting network information..."
        )

        network_data = get_network_info()

        print(
            "Checking disk health..."
        )

        disk_data = get_disk_health()

        print(
            "Analyzing Windows security events..."
        )

        security_data = analyze_security_events()

        print(
            "Checking Windows Firewall..."
        )

        firewall_data = get_firewall_status()

        print(
            "Reading scan history..."
        )

        scan_history = get_scan_history(
            limit=10
        )

        print(
            "Creating HTML report..."
        )

        report_path = generate_html_report(
            system_data,
            network_data,
            disk_data,
            security_data,
            firewall_data,
            scan_history
        )

        print(
            "\nHTML report generated successfully!"
        )

        print(
            "Report location:"
        )

        print(
            report_path
        )

        opened_report = open_report()

        if opened_report:

            print(
                "\nReport opened in your "
                "default web browser."
            )

        else:

            print(
                "\nReport was created but "
                "could not be opened automatically."
            )

        log_info(
            "HTML security report generated successfully."
        )

    except Exception as error:

        print(
            "\nError while generating "
            "HTML report."
        )

        print(
            "Error:",
            error
        )

        log_error(
            f"HTML report generation error: {error}"
        )


def main():

    setup_logger()

    create_database()

    log_info(
        "SecureDesk started."
    )

    print("=" * 50)

    print(
        "                 SECUREDESK"
    )

    print(
        "        IT SUPPORT & SECURITY MONITOR"
    )

    print("=" * 50)

    while True:

        print(
            "\n========== MAIN MENU =========="
        )

        print(
            "1. System Information"
        )

        print(
            "2. Network Diagnostics"
        )

        print(
            "3. Process Monitor"
        )

        print(
            "4. Disk Health"
        )

        print(
            "5. Windows Security Events"
        )

        print(
            "6. Windows Firewall Status"
        )

        print(
            "7. View Scan History"
        )

        print(
            "8. Generate HTML Security Report"
        )

        print(
            "9. Exit"
        )

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            show_system_info()

        elif choice == "2":

            show_network_info()

        elif choice == "3":

            show_process_info()

        elif choice == "4":

            show_disk_health()

        elif choice == "5":

            show_security_events()

        elif choice == "6":

            show_firewall_status()

        elif choice == "7":

            show_scan_history()

        elif choice == "8":

            show_html_report()

        elif choice == "9":

            log_info(
                "SecureDesk stopped."
            )

            print(
                "\nExiting SecureDesk..."
            )

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 9."
            )

            log_warning(
                f"Invalid menu choice entered: "
                f"{choice}"
            )


if __name__ == "__main__":

    main()