import psutil
import time

def get_services():

    services = []

    for service in psutil.win_service_iter():

        try:

            info = {
                "name": service.name(),
                "display_name": service.display_name(),
                "status": service.status(),
                "start_type": service.start_type(),
                "pid": service.pid()
            }

            services.append(info)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            FileNotFoundError
        ):
            pass

    return services

def display_services(services):
    print("WINDOWS SERVICES")

    print(
        f"{'SERVICE':<25}"
        f"{'DISPLAY NAME':<30}"
        f"{'STATUS':<12}"
        f"{'START TYPE':<15}"
        f"{'PID':<8}"
    )

    print("-" * 90)

    for service in services:

        pid = service["pid"]

        if pid is None:
            pid = "-"

        print(
            f"{service['name'][:23]:<25}"
            f"{service['display_name'][:28]:<30}"
            f"{service['status']:<12}"
            f"{service['start_type']:<15}"
            f"{str(pid):<8}"
        )

def show_running_services(services):

    running = [
        service
        for service in services
        if service["status"] == "running"
    ]

    print("\nRUNNING SERVICES")

    display_services(running)

def show_stopped_services(services):

    stopped = [
        service
        for service in services
        if service["status"] == "stopped"
    ]

    print("\nSTOPPED SERVICES")

    display_services(stopped)

def search_service(services):

    search = input(
        "\nEnter service name to search: "
    ).lower()

    found = False

    for service in services:

        if (
            search in service["name"].lower()
            or search in service["display_name"].lower()
        ):

            print("\n" + "-" * 60)

            print(
                f"Service:      {service['name']}"
            )

            print(
                f"Display Name: {service['display_name']}"
            )

            print(
                f"Status:       {service['status']}"
            )

            print(
                f"Start Type:   {service['start_type']}"
            )

            print(
                f"PID:          {service['pid']}"
            )

            found = True

    if not found:

        print("No matching service found.")

def service_status():

    name = input(
        "\nEnter exact service name: "
    )

    try:

        service = psutil.win_service_get(
            name
        )

        info = service.as_dict()

        print("SERVICE STATUS")

        print(
            f"Service:      {info['name']}"
        )

        print(
            f"Display Name: {info['display_name']}"
        )

        print(
            f"Status:       {info['status']}"
        )

        print(
            f"Start Type:   {info['start_type']}"
        )

        print(
            f"PID:          {info['pid']}"
        )

    except psutil.NoSuchProcess:

        print("Service not found.")

    except psutil.AccessDenied:

        print("Access denied.")

def service_change_detector():

    print("\nSERVICE CHANGE DETECTOR")
    print("Press Ctrl+C to stop.\n")

    previous = {
        service["name"]: service["status"]
        for service in get_services()
    }

    try:

        while True:

            time.sleep(2)

            current_services = get_services()

            current = {
                service["name"]: service["status"]
                for service in current_services
            }

            # Check for status changes
            for name in current:

                if name in previous:

                    if current[name] != previous[name]:

                        print(
                            f"[CHANGE] {name}: "
                            f"{previous[name]} → "
                            f"{current[name]}"
                        )

                else:

                    print(
                        f"[NEW SERVICE] {name}"
                    )

            # Check for removed services
            for name in previous:

                if name not in current:

                    print(
                        f"[REMOVED SERVICE] {name}"
                    )

            previous = current

    except KeyboardInterrupt:

        print("\nDetector stopped.")

def main():

    while True:
        print("WINDOWS SERVICE MONITOR")

        print("1. Show all services")
        print("2. Show running services")
        print("3. Show stopped services")
        print("4. Search service")
        print("5. Check service status")
        print("6. Service-change detector")
        print("7. Quit")

        choice = input("\nChoose an option: ")

        services = get_services()

        if choice == "1":

            display_services(services)

        elif choice == "2":

            show_running_services(services)

        elif choice == "3":

            show_stopped_services(services)

        elif choice == "4":

            search_service(services)

        elif choice == "5":

            service_status()

        elif choice == "6":

            service_change_detector()

        elif choice == "7":

            print("Exiting...")

            break

        else:

            print("Invalid choice.")

if __name__ == "__main__":
    main()