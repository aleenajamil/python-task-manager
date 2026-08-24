import psutil
def format_bytes(bytes):

    if bytes >= 1024 ** 3:
        return f"{bytes / (1024 ** 3):.2f} GB"

    elif bytes >= 1024 ** 2:
        return f"{bytes / (1024 ** 2):.2f} MB"

    elif bytes >= 1024:
        return f"{bytes / 1024:.2f} KB"

    else:
        return f"{bytes} B"

def show_system_memory():

    memory = psutil.virtual_memory()
    print("RAM")

    print(f"Total:       {format_bytes(memory.total)}")
    print(f"Used:        {format_bytes(memory.used)}")
    print(f"Available:   {format_bytes(memory.available)}")
    print(f"Usage:       {memory.percent:.1f}%")

    # Cached memory
    if hasattr(memory, "cached"):
        print(f"Cached:      {format_bytes(memory.cached)}")

def show_swap():

    swap = psutil.swap_memory()
    print("SWAP / PAGEFILE")
    print(f"Total:       {format_bytes(swap.total)}")
    print(f"Used:        {format_bytes(swap.used)}")
    print(f"Free:        {format_bytes(swap.free)}")
    print(f"Usage:       {swap.percent:.1f}%")

def get_process_memory():

    processes = []

    for proc in psutil.process_iter(
        ['pid', 'name']
    ):

        try:

            memory = proc.memory_info()

            rss = memory.rss
            vms = memory.vms

            processes.append({
                "pid": proc.pid,
                "name": proc.name(),
                "rss": rss,
                "vms": vms,
                "memory_percent": proc.memory_percent()
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return processes

def show_top_processes(processes):

    processes.sort(
        key=lambda process: process["rss"],
        reverse=True
    )

    print("TOP PROCESSES")

    print(
        f"{'PID':<8}"
        f"{'NAME':<25}"
        f"{'RSS':<15}"
        f"{'VMS':<15}"
    )

    for process in processes[:10]:

        print(
            f"{process['pid']:<8}"
            f"{process['name'][:23]:<25}"
            f"{format_bytes(process['rss']):<15}"
            f"{format_bytes(process['vms']):<15}"
        )

def inspect_process():

    choice = input(
        "\nEnter PID to inspect memory: "
    )

    try:
        pid = int(choice)

    except ValueError:
        print("Invalid PID.")
        return

    try:

        proc = psutil.Process(pid)

        memory = proc.memory_info()
        print("PROCESS MEMORY")
        print(f"Process:     {proc.name()}")
        print(f"PID:         {proc.pid}")

        print(
            f"RSS:         {format_bytes(memory.rss)}"
        )

        print(
            f"VMS:         {format_bytes(memory.vms)}"
        )

        print(
            f"Memory %:    {proc.memory_percent():.2f}%"
        )

    except psutil.NoSuchProcess:

        print("Process does not exist.")

    except psutil.AccessDenied:

        print("Access denied.")

def main():

    show_system_memory()

    show_swap()

    processes = get_process_memory()

    show_top_processes(processes)

    inspect_process()


if __name__ == "__main__":
    main()