import psutil


def get_disk_health():
    disk = psutil.disk_usage("C:\\")

    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    usage_percent = disk.percent

    if usage_percent >= 90:
        status = "CRITICAL"
        message = "Disk usage is extremely high."

    elif usage_percent >= 80:
        status = "WARNING"
        message = "Disk usage is high."

    else:
        status = "PASS"
        message = "Disk space is within a normal range."

    return {
        "total_gb": total_gb,
        "used_gb": used_gb,
        "free_gb": free_gb,
        "usage_percent": usage_percent,
        "status": status,
        "message": message
    }


if __name__ == "__main__":
    data = get_disk_health()

    print("\n===== DISK HEALTH =====")
    print(f"Total Space: {data['total_gb']:.2f} GB")
    print(f"Used Space: {data['used_gb']:.2f} GB")
    print(f"Free Space: {data['free_gb']:.2f} GB")
    print(f"Usage: {data['usage_percent']:.1f}%")
    print(f"Status: {data['status']}")
    print(f"Message: {data['message']}")