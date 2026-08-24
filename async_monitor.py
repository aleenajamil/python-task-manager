import asyncio
import psutil
from datetime import datetime

async def cpu_monitor():

    while True:

        cpu = psutil.cpu_percent(interval=None)

        print(
            f"[CPU] Usage: {cpu:.1f}%"
        )

        await asyncio.sleep(2)

async def ram_monitor():

    while True:

        memory = psutil.virtual_memory()

        print(
            f"[RAM] Usage: "
            f"{memory.percent:.1f}% | "
            f"Available: "
            f"{memory.available / (1024 ** 3):.2f} GB"
        )

        await asyncio.sleep(2)

async def disk_monitor():

    previous = psutil.disk_io_counters()

    while True:

        await asyncio.sleep(2)

        current = psutil.disk_io_counters()

        read_mb = (
            current.read_bytes
            - previous.read_bytes
        ) / (1024 ** 2)

        write_mb = (
            current.write_bytes
            - previous.write_bytes
        ) / (1024 ** 2)

        print(
            f"[DISK] "
            f"Read: {read_mb:.2f} MB | "
            f"Write: {write_mb:.2f} MB"
        )

        previous = current

async def network_monitor():

    previous = psutil.net_io_counters()

    while True:

        await asyncio.sleep(2)

        current = psutil.net_io_counters()

        received_mb = (
            current.bytes_recv
            - previous.bytes_recv
        ) / (1024 ** 2)

        sent_mb = (
            current.bytes_sent
            - previous.bytes_sent
        ) / (1024 ** 2)

        print(
            f"[NETWORK] "
            f"RX: {received_mb:.2f} MB | "
            f"TX: {sent_mb:.2f} MB"
        )

        previous = current

async def process_monitor():

    while True:

        processes = []

        for proc in psutil.process_iter(
            ['pid', 'name', 'memory_percent']
        ):

            try:

                processes.append(proc.info)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):
                pass

        processes.sort(
            key=lambda p: p['memory_percent'] or 0,
            reverse=True
        )

        top = processes[:5]

        print("\n[PROCESSES]")

        for process in top:

            print(
                f"PID {process['pid']:<7}"
                f"{str(process['name'])[:20]:<22}"
                f"RAM: "
                f"{process['memory_percent'] or 0:.2f}%"
            )

        await asyncio.sleep(3)


async def dashboard():

    while True:

        current_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        print(
            f"ASYNC SYSTEM MONITOR    {current_time}"
        )

        await asyncio.sleep(5)

async def main():

    print("ASYNC SYSTEM MONITOR")

    print(
        "Press Ctrl+C to stop.\n"
    )

    tasks = [

        asyncio.create_task(
            cpu_monitor()
        ),

        asyncio.create_task(
            ram_monitor()
        ),

        asyncio.create_task(
            disk_monitor()
        ),

        asyncio.create_task(
            network_monitor()
        ),

        asyncio.create_task(
            process_monitor()
        ),

        asyncio.create_task(
            dashboard()
        )
    ]

    try:

        await asyncio.gather(
            *tasks
        )

    except asyncio.CancelledError:

        print(
            "\nTasks cancelled."
        )

        for task in tasks:

            task.cancel()

if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        print(
            "\nMonitor stopped."
        )