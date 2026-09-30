import psutil


def get_top_processes(limit=10):
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"] or "Unknown",
                "cpu": info["cpu_percent"] or 0.0,
                "memory": info["memory_percent"] or 0.0
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda x: x["cpu"], reverse=True)

    return processes[:limit]


def show_processes():
    processes = get_top_processes()

    print("\n===== TOP RUNNING PROCESSES =====")
    print("-" * 65)
    print(f"{'PID':<10}{'Process':<30}{'CPU %':<10}{'Memory %':<10}")
    print("-" * 65)

    for process in processes:
        print(
            f"{process['pid']:<10}"
            f"{process['name'][:28]:<30}"
            f"{process['cpu']:<10.1f}"
            f"{process['memory']:<10.1f}"
        )


if __name__ == "__main__":
    show_processes()