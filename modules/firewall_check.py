import subprocess


def get_firewall_status():
    command = (
        "Get-NetFirewallProfile | "
        "Select-Object Name, Enabled | "
        "ConvertTo-Json"
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

        if result.returncode != 0:
            return {
                "status": "ERROR",
                "message": "Unable to read Windows Firewall status.",
                "profiles": []
            }

        output = result.stdout.strip()

        if not output:
            return {
                "status": "ERROR",
                "message": "No firewall information was returned.",
                "profiles": []
            }

        import json

        data = json.loads(output)

        if isinstance(data, dict):
            data = [data]

        profiles = []

        for profile in data:
            profiles.append({
                "name": profile.get("Name", "Unknown"),
                "enabled": profile.get("Enabled", False)
            })

        disabled_profiles = [
            profile["name"]
            for profile in profiles
            if not profile["enabled"]
        ]

        if disabled_profiles:
            status = "WARNING"
            message = (
                "One or more Windows Firewall profiles are disabled."
            )
        else:
            status = "PASS"
            message = "All detected Windows Firewall profiles are enabled."

        return {
            "status": status,
            "message": message,
            "profiles": profiles
        }

    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception) as error:
        return {
            "status": "ERROR",
            "message": f"Firewall check failed: {error}",
            "profiles": []
        }


def show_firewall_status():
    data = get_firewall_status()

    print("\n===== WINDOWS FIREWALL STATUS =====")

    for profile in data["profiles"]:
        status = "ENABLED" if profile["enabled"] else "DISABLED"

        print(f"{profile['name']}: {status}")

    print("\nOverall Status:", data["status"])
    print("Message:", data["message"])


if __name__ == "__main__":
    show_firewall_status()