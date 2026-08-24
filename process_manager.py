import subprocess
import psutil
import time
import os
import signal

child_process = None

def list_processes():
    print("RUNNING PROCESSES")

    print(
        f"{'PID':<8}"
        f"{'NAME':<30}"
        f"{'STATUS':<15}"
    )

    for proc in psutil.process_iter(
        ['pid', 'name', 'status']
    ):

        try:

            print(
                f"{proc.info['pid']:<8}"
                f"{proc.info['name'][:28]:<30}"
                f"{proc.info['status']:<15}"
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            pass

def search_process():

    search = input(
        "\nEnter process name to search: "
    ).lower()

    found = False

    for proc in psutil.process_iter(
        ['pid', 'name', 'status']
    ):

        try:

            name = proc.info['name']

            if name and search in name.lower():

                print(
                    f"PID: {proc.info['pid']} | "
                    f"Name: {name} | "
                    f"Status: {proc.info['status']}"
                )

                found = True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            pass

    if not found:

        print("No matching process found.")

def inspect_process():

    choice = input(
        "\nEnter PID to inspect: "
    )

    try:

        pid = int(choice)

    except ValueError:

        print("Invalid PID.")
        return

    try:

        proc = psutil.Process(pid)
        print("PROCESS INFORMATION")

        print(f"PID:          {proc.pid}")
        print(f"Name:         {proc.name()}")
        print(f"Status:       {proc.status()}")
        print(f"Executable:   {proc.exe()}")
        print(f"Username:     {proc.username()}")
        print(f"Parent PID:   {proc.ppid()}")
        print(f"Threads:      {proc.num_threads()}")

        print(
            f"Memory:       "
            f"{proc.memory_percent():.2f}%"
        )

        print(
            f"CPU:          "
            f"{proc.cpu_percent(interval=0.5):.2f}%"
        )

    except psutil.NoSuchProcess:

        print("Process no longer exists.")

    except psutil.AccessDenied:

        print("Access denied.")

def start_process():

    global child_process

    if child_process is not None:

        if child_process.poll() is None:

            print(
                "A child process is already running."
            )

            print(
                f"PID: {child_process.pid}"
            )

            return

    command = input(
        "\nEnter command to launch: "
    )

    if not command:

        print("No command entered.")
        return

    try:

        child_process = subprocess.Popen(
            command,
            shell=True
        )

        print("\nProcess started.")

        print(
            f"PID: {child_process.pid}"
        )

    except Exception as error:

        print(
            f"Could not start process: {error}"
        )

def stop_process():

    global child_process

    if child_process is None:

        print("No child process is being managed.")
        return

    if child_process.poll() is not None:

        print("The child process has already exited.")

        child_process = None

        return

    try:

        print(
            f"Stopping PID {child_process.pid}..."
        )

        child_process.terminate()

        child_process.wait(
            timeout=5
        )

        print("Process stopped.")

    except subprocess.TimeoutExpired:

        print(
            "Process did not stop gracefully."
        )

        child_process.kill()

        child_process.wait()

        print("Process terminated.")

    except Exception as error:

        print(
            f"Could not stop process: {error}"
        )

    finally:

        child_process = None

def wait_for_process():

    global child_process

    if child_process is None:

        print("No child process is being managed.")
        return

    print(
        f"Waiting for PID "
        f"{child_process.pid}..."
    )

    return_code = child_process.wait()

    print(
        f"Process finished."
    )

    print(
        f"Exit code: {return_code}"
    )

    child_process = None

def monitor_process():

    if child_process is None:

        print("No child process is being managed.")
        return

    pid = child_process.pid

    try:

        proc = psutil.Process(pid)

    except psutil.NoSuchProcess:

        print("Process no longer exists.")
        return
    
    print("PROCESS MONITOR")

    print("Press Ctrl+C to stop monitoring.\n")

    try:

        while child_process.poll() is None:

            try:

                cpu = proc.cpu_percent(
                    interval=1
                )

                memory = proc.memory_percent()

                print(
                    f"PID: {pid} | "
                    f"Status: {proc.status()} | "
                    f"CPU: {cpu:.2f}% | "
                    f"RAM: {memory:.2f}%"
                )

            except psutil.NoSuchProcess:

                print(
                    "Process disappeared."
                )

                break

    except KeyboardInterrupt:

        print("\nMonitoring stopped.")

def main():

    while True:

        print("PYTHON PROCESS MANAGER")

        print("1. List processes")
        print("2. Search process")
        print("3. Inspect process")
        print("4. Start child process")
        print("5. Stop child process")
        print("6. Wait for child process")
        print("7. Monitor child process")
        print("8. Quit")

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":

            list_processes()

        elif choice == "2":

            search_process()

        elif choice == "3":

            inspect_process()

        elif choice == "4":

            start_process()

        elif choice == "5":

            stop_process()

        elif choice == "6":

            wait_for_process()

        elif choice == "7":

            monitor_process()

        elif choice == "8":

            print("Exiting...")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":

    main()