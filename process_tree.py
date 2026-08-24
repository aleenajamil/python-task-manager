import psutil

processes = []

for proc in psutil.process_iter(['pid', 'ppid', 'name']):

    try:
        processes.append(proc.info)

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess
    ):
        pass

children = {}

for proc in processes:

    ppid = proc['ppid']

    if ppid not in children:
        children[ppid] = []

    children[ppid].append(proc)

all_pids = {
    proc['pid']
    for proc in processes
}

roots = []

for proc in processes:

    if proc['ppid'] not in all_pids:
        roots.append(proc)

def print_tree(proc, level=0):

    print(
        "    " * level +
        f"└── {proc['name']} "
        f"(PID: {proc['pid']})"
    )

    pid = proc['pid']

    if pid not in children:
        return

    for child in children[pid]:

        print_tree(
            child,
            level + 1
        )

print("PROCESS TREE")
for root in roots:

    print_tree(root)