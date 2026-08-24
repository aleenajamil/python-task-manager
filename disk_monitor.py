import psutil
import time

def show_partitions():
    print("DISK PARTITIONS")

    partitions = psutil.disk_partitions()

    for partition in partitions:

        print(f"\nDrive:       {partition.device}")
        print(f"Mountpoint:  {partition.mountpoint}")
        print(f"Filesystem:  {partition.fstype}")

        try:

            usage = psutil.disk_usage(
                partition.mountpoint
            )

            print(
                f"Total:       "
                f"{usage.total / (1024 ** 3):.2f} GB"
            )

            print(
                f"Used:        "
                f"{usage.used / (1024 ** 3):.2f} GB"
            )

            print(
                f"Free:        "
                f"{usage.free / (1024 ** 3):.2f} GB"
            )

            print(
                f"Usage:       "
                f"{usage.percent:.1f}%"
            )

        except PermissionError:

            print("Access denied.")

def get_disk_counters():

    return psutil.disk_io_counters()

def calculate_activity(
    old,
    new,
    interval
):

    read_bytes = (
        new.read_bytes - old.read_bytes
    )

    write_bytes = (
        new.write_bytes - old.write_bytes
    )

    read_ops = (
        new.read_count - old.read_count
    )

    write_ops = (
        new.write_count - old.write_count
    )

    read_speed = read_bytes / interval
    write_speed = write_bytes / interval

    read_ops_per_second = (
        read_ops / interval
    )

    write_ops_per_second = (
        write_ops / interval
    )

    return (
        read_speed,
        write_speed,
        read_ops_per_second,
        write_ops_per_second
    )

def monitor_disk():
    print("DISK ACTIVITY MONITOR")

    print("Measuring disk activity...\n")

    interval = 1

    old = get_disk_counters()

    time.sleep(interval)

    new = get_disk_counters()

    (
        read_speed,
        write_speed,
        read_ops,
        write_ops
    ) = calculate_activity(
        old,
        new,
        interval
    )

    print(
        f"Read:       "
        f"{read_speed / (1024 ** 2):.2f} MB/s"
    )

    print(
        f"Write:      "
        f"{write_speed / (1024 ** 2):.2f} MB/s"
    )

    print()

    print(
        f"Read Ops:   "
        f"{read_ops:.0f}/s"
    )

    print(
        f"Write Ops:  "
        f"{write_ops:.0f}/s"
    )

def show_raw_statistics():

    counters = get_disk_counters()
    print("DISK STATISTICS")

    print(
        f"Read count:      "
        f"{counters.read_count}"
    )

    print(
        f"Write count:     "
        f"{counters.write_count}"
    )

    print(
        f"Read bytes:      "
        f"{counters.read_bytes / (1024 ** 3):.2f} GB"
    )

    print(
        f"Write bytes:     "
        f"{counters.write_bytes / (1024 ** 3):.2f} GB"
    )

    print(
        f"Read time:       "
        f"{counters.read_time / 1000:.2f} seconds"
    )

    print(
        f"Write time:      "
        f"{counters.write_time / 1000:.2f} seconds"
    )
def main():

    show_partitions()

    show_raw_statistics()

    monitor_disk()


if __name__ == "__main__":
    main()