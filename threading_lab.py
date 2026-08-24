import threading
import time
import random
from queue import Queue

counter = 0

counter_lock = threading.Lock()

event = threading.Event()

semaphore = threading.Semaphore(2)

work_queue = Queue()

def worker(name):

    for i in range(5):

        print(
            f"[{name}] working... "
            f"step {i + 1}"
        )

        time.sleep(1)

    print(f"[{name}] finished.")


def basic_threads():

    print("\nStarting threads...\n")

    threads = []

    for i in range(3):

        thread = threading.Thread(
            target=worker,
            args=(f"T{i + 1}",)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print("\nAll threads finished.")

def thread_monitor():

    print("\nTHREAD MONITOR")

    def monitored_worker(name):

        print(
            f"[{name}] started | "
            f"Thread ID: {threading.get_ident()}"
        )

        time.sleep(random.uniform(2, 5))

        print(
            f"[{name}] finished"
        )

    threads = []

    for i in range(3):

        thread = threading.Thread(
            target=monitored_worker,
            args=(f"T{i + 1}",),
            name=f"Worker-{i + 1}"
        )

        threads.append(thread)

        thread.start()

    print("\nACTIVE THREADS:")

    for thread in threading.enumerate():

        print(
            f"Name: {thread.name:<15}"
            f"ID: {thread.ident}"
        )

    for thread in threads:

        thread.join()

    print("\nAll worker threads finished.")

def increase_counter():

    global counter

    for _ in range(100000):

        counter += 1


def race_condition():

    global counter

    counter = 0

    threads = []

    for _ in range(4):

        thread = threading.Thread(
            target=increase_counter
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print("\nRACE CONDITION TEST")

    print(
        f"Expected: 400000"
    )

    print(
        f"Actual:   {counter}"
    )

def increase_counter_safe():

    global counter

    for _ in range(100000):

        with counter_lock:

            counter += 1


def lock_demo():

    global counter

    counter = 0

    threads = []

    for _ in range(4):

        thread = threading.Thread(
            target=increase_counter_safe
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print("\nLOCK TEST")

    print(
        f"Expected: 400000"
    )

    print(
        f"Actual:   {counter}"
    )

def event_worker(name):

    print(
        f"[{name}] waiting for signal..."
    )

    event.wait()

    print(
        f"[{name}] received signal!"
    )


def event_demo():

    event.clear()

    threads = []

    for i in range(3):

        thread = threading.Thread(
            target=event_worker,
            args=(f"T{i + 1}",)
        )

        threads.append(thread)

        thread.start()

    time.sleep(2)

    print(
        "\nMAIN THREAD: Sending signal..."
    )

    event.set()

    for thread in threads:

        thread.join()

    print("All threads released.")

def semaphore_worker(name):

    print(
        f"[{name}] waiting for resource..."
    )

    with semaphore:

        print(
            f"[{name}] using resource"
        )

        time.sleep(2)

        print(
            f"[{name}] released resource"
        )


def semaphore_demo():

    threads = []

    for i in range(5):

        thread = threading.Thread(
            target=semaphore_worker,
            args=(f"T{i + 1}",)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print("\nSemaphore demo finished.")

def producer():

    for i in range(10):

        item = f"Item-{i + 1}"

        print(
            f"[PRODUCER] Created {item}"
        )

        work_queue.put(item)

        time.sleep(0.5)

    work_queue.put(None)

def consumer():

    while True:

        item = work_queue.get()

        if item is None:

            work_queue.task_done()

            break

        print(
            f"[CONSUMER] Processing {item}"
        )

        time.sleep(1)

        work_queue.task_done()


def producer_consumer():

    producer_thread = threading.Thread(
        target=producer
    )

    consumer_thread = threading.Thread(
        target=consumer
    )

    producer_thread.start()

    consumer_thread.start()

    producer_thread.join()

    consumer_thread.join()

    print(
        "\nProducer/consumer finished."
    )

def deadlock_demo():

    lock1 = threading.Lock()

    lock2 = threading.Lock()

    def worker_one():

        print("Worker 1: acquiring Lock 1")

        with lock1:

            time.sleep(1)

            print(
                "Worker 1: waiting for Lock 2"
            )

            with lock2:

                print(
                    "Worker 1: got both locks"
                )

    def worker_two():

        print("Worker 2: acquiring Lock 2")

        with lock2:

            time.sleep(1)

            print(
                "Worker 2: waiting for Lock 1"
            )

            with lock1:

                print(
                    "Worker 2: got both locks"
                )

    thread1 = threading.Thread(
        target=worker_one
    )

    thread2 = threading.Thread(
        target=worker_two
    )

    thread1.start()

    thread2.start()

    print(
        "\nTwo threads are now competing "
        "for locks."
    )

    print(
        "This demonstrates what a deadlock "
        "can look like."
    )

    thread1.join(timeout=3)

    thread2.join(timeout=3)

    if thread1.is_alive() or thread2.is_alive():

        print(
            "\nDEADLOCK DETECTED."
        )

        print(
            "The threads are waiting for "
            "each other's locks."
        )

def main():

    while True:
        print("PYTHON MULTITHREADING LAB")

        print("1. Basic threads")
        print("2. Thread monitor")
        print("3. Race condition")
        print("4. Lock")
        print("5. Event")
        print("6. Semaphore")
        print("7. Producer / Consumer")
        print("8. Deadlock demonstration")
        print("9. Quit")

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":

            basic_threads()

        elif choice == "2":

            thread_monitor()

        elif choice == "3":

            race_condition()

        elif choice == "4":

            lock_demo()

        elif choice == "5":

            event_demo()

        elif choice == "6":

            semaphore_demo()

        elif choice == "7":

            producer_consumer()

        elif choice == "8":

            deadlock_demo()

        elif choice == "9":

            print("Exiting...")

            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":

    main()