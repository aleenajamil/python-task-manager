# Python System & OS Internals Lab

A hands-on Python project for learning how operating systems work under the hood through system monitoring, process management, networking, concurrency, and Windows internals.

This repository contains a progression of practical projects built primarily with Python and `psutil`, gradually moving from basic system monitoring to processes, threads, multiprocessing, and asynchronous programming.

> The goal isn't just to use Python libraries — it's to understand what the operating system is actually doing underneath them.

---

## 🚀 Learning Roadmap

### Level 1 — Basic OS Monitoring

Learn how to inspect running processes.

- List running processes
- Process IDs (PID)
- Process names
- Executable paths
- Process status
- CPU usage
- RAM usage
- Creation time
- Username
- Number of threads
- Parent PID
- Child processes

**Project:** Basic Process Monitor

---

### Level 2 — CPU Internals

Investigate CPU information and utilization.

- Overall CPU utilization
- Per-core utilization
- CPU frequency
- Physical vs logical cores
- CPU count
- CPU load
- CPU time
- User CPU time
- System CPU time
- Idle time
- Interrupt statistics where available
- Context switches where available

**Project:** Live CPU Monitor

---

### Level 3 — Process Internals

Build a more detailed process explorer.

For each process:

- PID
- PPID
- Name
- Executable
- Command line
- Username
- Status
- Creation time
- CPU usage
- Memory usage
- RSS
- VMS
- Threads
- Open files
- Network connections
- CPU times
- Memory maps

Additional features:

- Search processes
- Sort by CPU
- Sort by RAM
- Find process by PID
- Find processes by name
- Find parent processes
- Find child processes

**Project:** Process Explorer

---

### Level 4 — Process Tree

Explore parent/child relationships between processes.

Learn:

- PID
- PPID
- Recursion
- Dictionaries
- Tree structures
- Parent/child process relationships
- OS process architecture

**Project:** Process Tree Viewer

Example:

```text
System
├── explorer.exe
│   ├── application.exe
│   └── application.exe
├── chrome.exe
│   ├── chrome.exe
│   ├── chrome.exe
│   └── chrome.exe
└── python.exe
    └── subprocess.exe
