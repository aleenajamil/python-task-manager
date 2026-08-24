import psutil

def show_threads(proc):

    print("\n" + "=" * 60)
    print("THREAD MONITOR")
    print("=" * 60)

    print(f"Process: {proc.name()}")
    print(f"PID:     {proc.pid}")

    print("\n")
    print(
        f"{'TID':<12}"
        f"{'USER TIME':<18}"
        f"{'SYSTEM TIME':<18}"
    )

    print("-" * 48)

    try:

        threads = proc.threads()

        for thread in threads:

            print(
                f"{thread.id:<12}"
                f"{thread.user_time:<18.2f}"
                f"{thread.system_time:<18.2f}"
            )

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess
    ):

        print("Unable to access threads.")

def find_process():

    choice = input(
        "\nEnter PID of the process to inspect: "
    )

    try:
        pid = int(choice)

    except ValueError:
        print("Invalid PID.")
        return

    try:

        proc = psutil.Process(pid)

        show_threads(proc)

    except psutil.NoSuchProcess:

        print("Process does not exist.")

    except psutil.AccessDenied:

        print("Access denied.")

def main():
    print("PROCESS THREAD MONITOR")

    find_process()


if __name__ == "__main__":
    main()