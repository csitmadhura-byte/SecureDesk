import subprocess


def count_security_events(event_id, hours=24):
    command = (
        f"$start=(Get-Date).AddHours(-{hours}); "
        f"try {{ "
        f"@(Get-WinEvent -FilterHashtable "
        f"@{{LogName='Security'; Id={event_id}; StartTime=$start}}).Count "
        f"}} catch {{ 0 }}"
    )

    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                command
            ],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode == 0:
            output = result.stdout.strip()

            if output:
                return int(output)

        return 0

    except (subprocess.TimeoutExpired, ValueError):
        return 0


def analyze_security_events(hours=24, threshold=5):
    successful_logins = count_security_events(4624, hours)
    failed_logins = count_security_events(4625, hours)

    if failed_logins >= threshold:
        status = "WARNING"
        message = (
            "Multiple failed login attempts detected. "
            "Manual investigation is recommended."
        )
    else:
        status = "PASS"
        message = "No unusual number of failed login attempts detected."

    return {
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "threshold": threshold,
        "status": status,
        "message": message
    }


if __name__ == "__main__":
    data = analyze_security_events()

    print("\n===== WINDOWS SECURITY EVENTS =====")
    print("Analysis Period: Last 24 hours")
    print("Successful Logins (4624):", data["successful_logins"])
    print("Failed Logins (4625):", data["failed_logins"])
    print("Threshold:", data["threshold"])
    print("Status:", data["status"])
    print("Message:", data["message"])