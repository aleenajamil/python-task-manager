import multiprocessing
import threading
import time
from concurrent.futures import ProcessPoolExecutor

def cpu_work(number):

    total = 0

    for i in range(number):

        total += i * i

    return total

def threading_test():

    print("\nTHREADING TEST")

    start = time.perf_counter()

    threads = []

    for _ in range(4):

        thread = threading.Thread(
            target=cpu_work,
            args=(5_000_000,)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    end = time.perf_counter()

    print(
        f"Time: {end - start:.2f} seconds"
    )

def multiprocessing_test():

    print("\nMULTIPROCESSING TEST")

    start = time.perf_counter()

    processes = []

    for _ in range(4):

        process = multiprocessing.Process(
            target=cpu_work,
            args=(5_000_000,)
        )

        processes.append(process)

        process.start()

    for process in processes:

        process.join()

    end = time.perf_counter()

    print(
        f"Time: {end - start:.2f} seconds"
    )

def process_pool_test():

    print("\nPROCESS POOL TEST")
    print("=" * 60)

    numbers = [
        5_000_000,
        5_000_000,
        5_000_000,
        5_000_000
    ]

    start = time.perf_counter()

    with ProcessPoolExecutor(
        max_workers=4
    ) as executor:

        results = list(
            executor.map(
                cpu_work,
                numbers
            )
        )

    end = time.perf_counter()

    print(
        f"Time: {end - start:.2f} seconds"
    )

    print(
        f"Results received: {len(results)}"
    )

def worker():

    print(
        f"Child Process PID: "
        f"{multiprocessing.current_process().pid}"
    )


def process_demo():

    print("\nPROCESS INFORMATION")
    print("=" * 60)

    print(
        f"Main Process PID: "
        f"{multiprocessing.current_process().pid}"
    )

    processes = []

    for _ in range(4):

        process = multiprocessing.Process(
            target=worker
        )

        processes.append(process)

        process.start()

    for process in processes:

        process.join()

    print("\nAll child processes finished.")

def main():

    while True:
        print("PYTHON MULTIPROCESSING LAB")

        print("1. Show processes")
        print("2. Threading CPU test")
        print("3. Multiprocessing CPU test")
        print("4. ProcessPoolExecutor test")
        print("5. Run all")
        print("6. Quit")

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":

            process_demo()

        elif choice == "2":

            threading_test()

        elif choice == "3":

            multiprocessing_test()

        elif choice == "4":

            process_pool_test()

        elif choice == "5":

            process_demo()

            threading_test()

            multiprocessing_test()

            process_pool_test()

        elif choice == "6":

            print("Exiting...")

            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":

    main()