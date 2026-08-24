import win32evtlog
import win32con
from datetime import datetime

def get_level(event_type):

    if event_type == win32con.EVENTLOG_INFORMATION_TYPE:
        return "INFO"

    elif event_type == win32con.EVENTLOG_WARNING_TYPE:
        return "WARNING"

    elif event_type == win32con.EVENTLOG_ERROR_TYPE:
        return "ERROR"

    elif event_type == win32con.EVENTLOG_AUDIT_SUCCESS:
        return "AUDIT SUCCESS"

    elif event_type == win32con.EVENTLOG_AUDIT_FAILURE:
        return "AUDIT FAILURE"

    else:
        return "UNKNOWN"

def read_events(log_name="System", max_events=50):

    server = None

    handle = win32evtlog.OpenEventLog(
        server,
        log_name
    )

    flags = (
        win32evtlog.EVENTLOG_BACKWARDS_READ
        | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    )

    events = []

    try:

        while len(events) < max_events:

            records = win32evtlog.ReadEventLog(
                handle,
                flags,
                0
            )

            if not records:
                break

            for event in records:

                events.append(event)

                if len(events) >= max_events:
                    break

    finally:

        win32evtlog.CloseEventLog(handle)

    return events

def display_events(events):
    print("WINDOWS EVENT LOG")

    print(
        f"{'TIME':<22}"
        f"{'LEVEL':<15}"
        f"{'SOURCE':<35}"
    )

    print("-" * 90)

    for event in events:

        time = event.TimeGenerated

        # Convert Windows time to Python datetime
        time = time.Format()

        level = get_level(
            event.EventType
        )

        source = event.SourceName

        print(
            f"{time:<22}"
            f"{level:<15}"
            f"{source:<35}"
        )

def show_event_details(events):
    print("EVENT DETAILS")

    for event in events:

        print("\n" + "-" * 70)

        print(
            f"Time:        "
            f"{event.TimeGenerated.Format()}"
        )

        print(
            f"Source:      "
            f"{event.SourceName}"
        )

        print(
            f"Event ID:    "
            f"{event.EventID & 0xFFFF}"
        )

        print(
            f"Level:       "
            f"{get_level(event.EventType)}"
        )

        print(
            f"Computer:    "
            f"{event.ComputerName}"
        )

        if event.StringInserts:

            print("Message:")

            for message in event.StringInserts:

                print(
                    f"  {message}"
                )

def filter_by_level(events):

    print("\n")
    print("1. Information")
    print("2. Warning")
    print("3. Error")
    print("4. Critical")

    choice = input(
        "\nChoose level: "
    )

    levels = {
        "1": "INFO",
        "2": "WARNING",
        "3": "ERROR",
        "4": "CRITICAL"
    }

    selected = levels.get(choice)

    if selected is None:

        print("Invalid choice.")
        return

    filtered = [
        event
        for event in events
        if get_level(event.EventType) == selected
    ]

    print(
        f"\nFound {len(filtered)} {selected} events."
    )

    display_events(filtered)

def main():

    while True:
        print("SYSTEM EVENT MONITOR")

        print("1. Show recent System events")
        print("2. Show event details")
        print("3. Filter by level")
        print("4. Quit")

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":

            events = read_events(
                "System",
                50
            )

            display_events(events)

        elif choice == "2":

            events = read_events(
                "System",
                20
            )

            show_event_details(events)

        elif choice == "3":

            events = read_events(
                "System",
                100
            )

            filter_by_level(events)

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()