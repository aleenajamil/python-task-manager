from pathlib import Path
from datetime import datetime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMonitorHandler(FileSystemEventHandler):

    def get_time(self):

        return datetime.now().strftime("%H:%M:%S")

    def on_created(self, event):

        if not event.is_directory:

            print(
                f"[{self.get_time()}] "
                f"CREATED   {event.src_path}"
            )

    def on_modified(self, event):

        if not event.is_directory:

            print(
                f"[{self.get_time()}] "
                f"MODIFIED  {event.src_path}"
            )

    def on_deleted(self, event):

        if not event.is_directory:

            print(
                f"[{self.get_time()}] "
                f"DELETED   {event.src_path}"
            )

    def on_moved(self, event):

        if not event.is_directory:

            print(
                f"[{self.get_time()}] "
                f"MOVED     {event.src_path}"
            )

            print(
                f"            → {event.dest_path}"
            )


def monitor_folder(folder):

    path = Path(folder)

    if not path.exists():

        print("Folder does not exist.")
        return

    if not path.is_dir():

        print("That path is not a folder.")
        return

    handler = FileMonitorHandler()

    observer = Observer()

    observer.schedule(
        handler,
        str(path),
        recursive=True
    )

    observer.start()
    print("REAL-TIME FILE MONITOR")

    print(f"Watching: {path.resolve()}")
    print("Press Ctrl+C to stop.\n")

    try:

        while True:

            # Keep the program alive
            observer.join(1)

    except KeyboardInterrupt:

        print("\nStopping monitor...")

        observer.stop()

    observer.join()

    print("Monitor stopped.")

def main():

    folder = input(
        "Enter folder to monitor: "
    )

    monitor_folder(folder)


if __name__ == "__main__":
    main()