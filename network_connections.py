import psutil
import socket


def get_protocol(connection):

    if connection.type == socket.SOCK_STREAM:
        return "TCP"

    elif connection.type == socket.SOCK_DGRAM:
        return "UDP"

    else:
        return "OTHER"


def show_connections():

    print("\nNETWORK CONNECTIONS")

    print(
        f"{'PID':<8}"
        f"{'PROCESS':<25}"
        f"{'LOCAL':<25}"
        f"{'REMOTE':<25}"
        f"{'STATUS':<15}"
        f"{'PROTOCOL':<10}"
    )

    for connection in psutil.net_connections(
        kind="inet"
    ):

        try:

            pid = connection.pid

            if pid is None:

                process_name = "Unknown"

            else:

                try:

                    process_name = (
                        psutil.Process(pid).name()
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied
                ):

                    process_name = "Unknown"

            # Local address

            if connection.laddr:

                local = (
                    f"{connection.laddr.ip}:"
                    f"{connection.laddr.port}"
                )

            else:

                local = "-"

            # Remote address

            if connection.raddr:

                remote = (
                    f"{connection.raddr.ip}:"
                    f"{connection.raddr.port}"
                )

            else:

                remote = "-"

            protocol = get_protocol(connection)

            print(
                f"{str(pid):<8}"
                f"{process_name[:23]:<25}"
                f"{local:<25}"
                f"{remote:<25}"
                f"{connection.status:<15}"
                f"{protocol:<10}"
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):

            pass


def find_process_connections():

    search = input(
        "\nEnter process name or PID: "
    )

    print("\nMATCHING CONNECTIONS")

    for connection in psutil.net_connections(
        kind="inet"
    ):

        try:

            pid = connection.pid

            if pid is None:

                continue

            process = psutil.Process(pid)

            name = process.name()

            if (
                search.lower() in name.lower()
                or search == str(pid)
            ):

                if connection.laddr:

                    local = (
                        f"{connection.laddr.ip}:"
                        f"{connection.laddr.port}"
                    )

                else:

                    local = "-"

                if connection.raddr:

                    remote = (
                        f"{connection.raddr.ip}:"
                        f"{connection.raddr.port}"
                    )

                else:

                    remote = "-"

                print(
                    f"PID: {pid}"
                )

                print(
                    f"Process: {name}"
                )

                print(
                    f"Local: {local}"
                )

                print(
                    f"Remote: {remote}"
                )

                print(
                    f"Status: {connection.status}"
                )

                print(
                    f"Protocol: "
                    f"{get_protocol(connection)}"
                )

                print("-" * 50)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):

            pass


def main():

    while True:
        print("NETWORK CONNECTION MONITOR")

        print("1. Show all connections")
        print("2. Find process connections")
        print("3. Quit")

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":

            show_connections()

        elif choice == "2":

            find_process_connections()

        elif choice == "3":

            print("Exiting...")

            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":

    main()