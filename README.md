# Python System & OS Internals 

A hands-on Python project exploring operating systems, system monitoring, processes, networking, and concurrency.

The project progresses from basic system monitoring to more advanced OS and Python concepts.

---

## 🚀 Levels

### Level 1 — Basic OS Monitoring
- Running processes
- PID, name, status
- CPU & RAM usage
- Executable path
- Threads
- Parent/child processes

### Level 2 — CPU Internals
- CPU utilization
- Per-core usage
- CPU frequency
- Physical & logical cores
- CPU times
- Context switches

### Level 3 — Process Internals
- Process information
- Command lines
- RSS & VMS
- Open files
- Network connections
- CPU & memory details
- Process searching and sorting

### Level 4 — Process Tree
- PID / PPID
- Parent-child relationships
- Recursion
- Process trees

### Level 5 — Threads
- Thread IDs
- User/system CPU time
- Process → thread relationships

### Level 6 — Memory
- RAM usage
- Available memory
- Swap/pagefile
- RSS & VMS
- Virtual vs physical memory

### Level 7 — Disk Internals
- Disk partitions
- Capacity & free space
- Read/write activity
- Read/write operations

### Level 8 — Network Internals
- Network interfaces
- IP & MAC addresses
- Bytes and packets
- Errors and dropped packets

### Level 9 — Network Connections
- Processes and sockets
- Local/remote IPs
- Ports
- Connection status
- TCP/UDP

### Level 10 — Windows Services
- Service status
- Start type
- Service search
- Service monitoring
- Change detection

### Level 11 — Windows Event Logs
- Information
- Warnings
- Errors
- Critical events

### Level 12 — File-System Monitoring
- File creation
- Modification
- Deletion
- Movement
- Event-driven monitoring

### Level 13 — Process Control
- `subprocess`
- Starting/stopping processes
- Process monitoring
- Process lifecycles

### Level 14 — Multithreading
- Threads
- Locks
- Events
- Semaphores
- Queues
- Race conditions
- Deadlocks
- Producer/consumer

### Level 15 — Multiprocessing
- `multiprocessing`
- `ProcessPoolExecutor`
- Process creation
- CPU-bound workloads
- Threading vs multiprocessing

### Level 16 — Async Python
- `asyncio`
- `async` / `await`
- Tasks
- Futures
- Event loops
- Concurrent system monitoring

---

## 🛠️ Technologies

- Python 3
- `psutil`
- `watchdog`
- `threading`
- `multiprocessing`
- `asyncio`
- `subprocess`
- `socket`
- `pathlib`

---

## 🎯 Goal

To understand how Python interacts with the operating system by building practical tools instead of learning system concepts purely through theory.

```text
Processes
   ↓
Threads
   ↓
Memory
   ↓
CPU
   ↓
Disk
   ↓
Networking
   ↓
Concurrency
   ↓
Async Python
```
---

## 🖥️ Platform

Primarily developed and tested on **Windows**.

Some functionality may behave differently on Linux/macOS due to OS-specific features.

---

## ⚠️ Disclaimer

For learning, system monitoring, and authorized experimentation only.
