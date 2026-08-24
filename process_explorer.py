import psutil
from datetime import datetime

def get_process_info(proc):

    try:

        pid = proc.pid
        ppid = proc.ppid()
        name = proc.name()

        try:
            executable = proc.exe()
        except psutil.AccessDenied:
            executable = "Access Denied"

        try:
            command_line = proc.cmdline()
        except psutil.AccessDenied:
            command_line = ["Access Denied"]

        try:
            username = proc.username()
        except psutil.AccessDenied:
            username = "Access Denied"
        
        status = proc.status()

        try:
            create_time = datetime.fromtimestamp(
                proc.create_time()
            ).strftime("%Y-%m-%d %H:%M:%S")
        except psutil.AccessDenied:
            create_time = "Access Denied"

        try:
            cpu = proc.cpu_percent(interval=0.1)
        except psutil.AccessDenied:
            cpu = 0
        try:
            memory_percent = proc.memory_percent()
            memory_info = proc.memory_info()

            rss = memory_info.rss / (1024 * 1024)
            vms = memory_info.vms / (1024 * 1024)

        except psutil.AccessDenied:
            memory_percent = 0
            rss = 0
            vms = 0
        try:
            threads = proc.num_threads()
        except psutil.AccessDenied:
            threads = 0

        try:
            open_files = proc.open_files()
        except psutil.AccessDenied:
            open_files = []

        try:
            connections = proc.net_connections()
        except psutil.AccessDenied:
            connections = []

        try:
            cpu_times = proc.cpu_times()
        except psutil.AccessDenied:
            cpu_times = None

        try:
            memory_maps = proc.memory_maps()
        except psutil.AccessDenied:
            memory_maps = []

        return {
            "pid": pid,
            "ppid": ppid,
            "name": name,
            "executable": executable,
            "command_line": command_line,
            "username": username,
            "status": status,
            "create_time": create_time,
            "cpu": cpu,
            "memory_percent": memory_percent,
            "rss": rss,
            "vms": vms,
            "threads": threads,
            "open_files": open_files,
            "connections": connections,
            "cpu_times": cpu_times,
            "memory_maps": memory_maps
        }

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess
    ):
        return None

def display_process(info):
    print("PROCESS INFORMATION")

    print(f"PID:              {info['pid']}")
    print(f"PPID:             {info['ppid']}")
    print(f"Name:             {info['name']}")
    print(f"Executable:       {info['executable']}")

    print(f"Command line:     {' '.join(info['command_line'])}")

    print(f"Username:         {info['username']}")
    print(f"Status:           {info['status']}")
    print(f"Create time:      {info['create_time']}")

    print(f"CPU:              {info['cpu']:.2f}%")
    print(f"Memory:           {info['memory_percent']:.2f}%")
    print(f"RSS:              {info['rss']:.2f} MB")
    print(f"VMS:              {info['vms']:.2f} MB")

    print(f"Threads:          {info['threads']}")

    if info["cpu_times"]:
        print("\nCPU TIMES")
        print(f"User:             {info['cpu_times'].user:.2f} sec")
        print(f"System:           {info['cpu_times'].system:.2f} sec")

    # Open files
    print("\nOPEN FILES")

    if info["open_files"]:
        for file in info["open_files"]:
            print(file.path)
    else:
        print("None / Access Denied")

    print("\nNETWORK CONNECTIONS")

    if info["connections"]:
        for connection in info["connections"]:
            print(connection)
    else:
        print("None / Access Denied")

    # Memory maps
    print("\nMEMORY MAPS")

    if info["memory_maps"]:
        for memory in info["memory_maps"][:10]:
            print(memory.path)
    else:
        print("None / Access Denied")

def get_all_processes():

    processes = []

    for proc in psutil.process_iter():

        info = get_process_info(proc)

        if info:
            processes.append(info)

    return processes

def display_process_table(processes):

    print("PROCESS EXPLORER")

    print(
        f"{'PID':<8}"
        f"{'PPID':<8}"
        f"{'NAME':<25}"
        f"{'CPU':<10}"
        f"{'RAM':<10}"
        f"{'THREADS':<10}"
    )

    for process in processes:

        print(
            f"{process['pid']:<8}"
            f"{process['ppid']:<8}"
            f"{process['name'][:23]:<25}"
            f"{process['cpu']:<10.1f}"
            f"{process['memory_percent']:<10.2f}"
            f"{process['threads']:<10}"
        )

def find_by_pid(processes):

    pid = input("Enter PID: ")

    try:
        pid = int(pid)
    except ValueError:
        print("Invalid PID.")
        return

    for process in processes:

        if process["pid"] == pid:
            display_process(process)
            return

    print("Process not found.")

def find_by_name(processes):

    name = input("Enter process name: ").lower()

    found = False

    for process in processes:

        if name in process["name"].lower():

            print(
                f"PID: {process['pid']} | "
                f"Name: {process['name']} | "
                f"CPU: {process['cpu']:.1f}% | "
                f"RAM: {process['memory_percent']:.2f}%"
            )

            found = True

    if not found:
        print("No matching processes found.")

def sort_by_cpu(processes):

    processes.sort(
        key=lambda process: process["cpu"],
        reverse=True
    )

    display_process_table(processes)


def sort_by_ram(processes):

    processes.sort(
        key=lambda process: process["memory_percent"],
        reverse=True
    )

    display_process_table(processes)

def find_parent(processes):

    pid = int(input("Enter PID: "))

    selected = None

    for process in processes:

        if process["pid"] == pid:
            selected = process
            break

    if not selected:
        print("Process not found.")
        return

    parent_pid = selected["ppid"]

    for process in processes:

        if process["pid"] == parent_pid:

            print(
                f"\nParent Process:\n"
                f"PID: {process['pid']}\n"
                f"Name: {process['name']}"
            )

            return

    print("Parent process not found.")

def find_children(processes):

    pid = int(input("Enter PID: "))

    found = False

    print("\nChild Processes:")

    for process in processes:

        if process["ppid"] == pid:

            print(
                f"PID: {process['pid']} | "
                f"Name: {process['name']}"
            )

            found = True

    if not found:
        print("No child processes found.")

def main():

    while True:

        processes = get_all_processes()

        print("\n")
        print("=" * 50)
        print("PROCESS EXPLORER")
        print("=" * 50)

        print("1. Show all processes")
        print("2. Find process by PID")
        print("3. Find process by name")
        print("4. Sort by CPU")
        print("5. Sort by RAM")
        print("6. Find parent process")
        print("7. Find child processes")
        print("8. Quit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            display_process_table(processes)

        elif choice == "2":
            find_by_pid(processes)

        elif choice == "3":
            find_by_name(processes)

        elif choice == "4":
            sort_by_cpu(processes)

        elif choice == "5":
            sort_by_ram(processes)

        elif choice == "6":
            find_parent(processes)

        elif choice == "7":
            find_children(processes)

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()