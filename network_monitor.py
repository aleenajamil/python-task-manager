import psutil
import socket
import ipaddress

def show_interfaces():
    print("NETWORK INTERFACES")

    interfaces = psutil.net_if_addrs()

    for interface, addresses in interfaces.items():

        print(f"\nInterface: {interface}")

        for address in addresses:

            if address.family == socket.AF_INET:

                print(f"IPv4:       {address.address}")
                print(f"Netmask:    {address.netmask}")

                # Use ipaddress to examine the IP
                try:

                    ip = ipaddress.ip_address(
                        address.address
                    )

                    print(
                        f"Private IP: {ip.is_private}"
                    )

                except ValueError:
                    pass

            elif address.family == socket.AF_INET6:

                print(
                    f"IPv6:       {address.address}"
                )

            elif address.family == psutil.AF_LINK:

                print(
                    f"MAC:        {address.address}"
                )

def show_network_traffic():
    print("NETWORK TRAFFIC")

    counters = psutil.net_io_counters(
        pernic=True
    )

    for interface, stats in counters.items():

        print(f"\n{interface}")
        print("-" * 50)

        print(
            f"Bytes sent:       "
            f"{stats.bytes_sent / (1024 ** 2):.2f} MB"
        )

        print(
            f"Bytes received:   "
            f"{stats.bytes_recv / (1024 ** 2):.2f} MB"
        )

        print(
            f"Packets sent:     "
            f"{stats.packets_sent}"
        )

        print(
            f"Packets received: "
            f"{stats.packets_recv}"
        )

        print(
            f"Errors sent:      "
            f"{stats.errout}"
        )

        print(
            f"Errors received:  "
            f"{stats.errin}"
        )

        print(
            f"Dropped sent:     "
            f"{stats.dropout}"
        )

        print(
            f"Dropped received: "
            f"{stats.dropin}"
        )

def show_connections():
    print("NETWORK CONNECTIONS")

    try:

        connections = psutil.net_connections(
            kind="inet"
        )

        for connection in connections:

            print(
                f"PID: {connection.pid} | "
                f"Status: {connection.status} | "
                f"Local: {connection.laddr} | "
                f"Remote: {connection.raddr}"
            )

    except psutil.AccessDenied:

        print("Access denied.")

def show_host_information():
    print("HOST INFORMATION")

    hostname = socket.gethostname()

    print(f"Hostname: {hostname}")

    try:

        local_ip = socket.gethostbyname(
            hostname
        )

        print(f"Local IP: {local_ip}")

    except socket.gaierror:

        print("Unable to determine local IP.")

def main():

    show_host_information()

    show_interfaces()

    show_network_traffic()

    show_connections()


if __name__ == "__main__":
    main()