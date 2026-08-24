import psutil
from datetime import datetime

print(f"{'PID':<8}{'NAME':<25}{'CPU':<10}{'RAM':<12}{'STATUS':<15}")

for proc in psutil.process_iter():

    try:
        # Creation time
        created = datetime.fromtimestamp(
            proc.create_time()
        ).strftime('%Y-%m-%d %H:%M:%S')

        cpu = proc.cpu_percent(interval=0.1)
        ram = proc.memory_info().rss / (1024 * 1024)
        print(
            f"{proc.pid:<8}"
            f"{proc.name()[:23]:<25}"
            f"{cpu:<10.1f}"
            f"{ram:<12.1f}"
            f"{proc.status():<15}"
        )

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass

print("DETAILED PROCESS INFORMATION")

for proc in psutil.process_iter():

    try:
        created = datetime.fromtimestamp(
            proc.create_time()
        ).strftime('%Y-%m-%d %H:%M:%S')

        # Get child processes
        children = proc.children(recursive=True)

        print(f"""
PID: {proc.pid}

Name: {proc.name()}

Executable: {proc.exe()}

Status: {proc.status()}

CPU Usage: {proc.cpu_percent(interval=0.1):.1f}%

RAM Usage: {proc.memory_info().rss / (1024 * 1024):.2f} MB

Created: {created}

Username: {proc.username()}

Threads: {proc.num_threads()}

Parent PID: {proc.ppid()}

Children: {[child.pid for child in children]}

""")

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass