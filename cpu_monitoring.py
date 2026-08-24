import psutil
import time

print("CPU INFORMATION")

physical_cores = psutil.cpu_count(logical=False)

logical_cpus = psutil.cpu_count(logical=True)

print(f"Physical cores: {physical_cores}")
print(f"Logical CPUs:   {logical_cpus}")

frequency = psutil.cpu_freq()

if frequency:
    print(f"Frequency:      {frequency.current / 1000:.2f} GHz")
else:
    print("Frequency:      Not available")

print("CPU USAGE")

overall_usage = psutil.cpu_percent(interval=1)

print(f"Overall CPU:    {overall_usage:.1f}%")

core_usage = psutil.cpu_percent(
    interval=1,
    percpu=True
)

for i, usage in enumerate(core_usage):
    print(f"Core {i}:         {usage:.1f}%")

print("CPU TIMES")
times = psutil.cpu_times()

print(f"User time:      {times.user:.2f} seconds")
print(f"System time:    {times.system:.2f} seconds")
print(f"Idle time:      {times.idle:.2f} seconds")

if hasattr(times, "interrupt"):
    print(f"Interrupt time: {times.interrupt:.2f} seconds")

print("CPU STATISTICS")

stats = psutil.cpu_stats()

print(f"Context switches: {stats.ctx_switches}")

if hasattr(stats, "interrupts"):
    print(f"Interrupts:       {stats.interrupts}")

if hasattr(stats, "soft_interrupts"):
    print(f"Soft interrupts:  {stats.soft_interrupts}")