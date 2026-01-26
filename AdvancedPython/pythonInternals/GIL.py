"""
GIL: Global Interpreter Lock

Python uses reference counting for memory management. 
Every object tracks how many references point to it:
"""
x = [1, 2, 3]      # Reference count = 1
y = x              # Reference count = 2
z = x              # Reference count = 3
del y              # Reference count = 2
del x              # Reference count = 1
del z              # Reference count = 0 → Object deleted!
"""
If two threads modify reference counts at the same time, you get a race condition
Thread 1: Read refcount (5) → Decrement → Write (4)
Thread 2: Read refcount (5) → Decrement → Write (4)

"""
#space
#space
#space
"""
Result: Both decremented, but should be 3!
Outcome: MEMORY CORRUPTION

The GIL is a mutex (lock) that ensures only ONE thread at a time executes Python bytecode.
Thread 1: [Holds GIL] Execute bytecode
Thread 2: [Waits for GIL] ....waiting....
Thread 1: [Releases GIL] 
Thread 2: [Acquires GIL] Execute bytecode
"""
#space
#space
#space
"""
The reason  threading is used in python is because it allows for concurrent execution of code.
This is useful for I/O-bound tasks like file downloads.
Eventhough the GIL prevents true parallelism for CPU work, it allows for concurrent execution of code.
for example in the following code:

"""

import threading
import time

def download_file(url, thread_name):
    print(f"{thread_name}: Starting download...")
    time.sleep(2)  # Simulates network I/O (waiting for file)
    print(f"{thread_name}: Download complete!")

# Single-threaded
print("=== SINGLE-THREADED ===")
start = time.time()
download_file("url1", "Thread 1")
download_file("url2", "Thread 2")
elapsed = time.time() - start
print(f"Total time: {elapsed:.1f}s\n")

# Multi-threaded
print("=== MULTI-THREADED ===")
start = time.time()
t1 = threading.Thread(target=download_file, args=("url1", "Thread 1"))
t2 = threading.Thread(target=download_file, args=("url2", "Thread 2"))
t1.start()
t2.start()
t1.join()
t2.join()
elapsed = time.time() - start
print(f"Total time: {elapsed:.1f}s")

"""
MULTI-THREADED EXECUTION:
Single-threaded: 2 files → 4 seconds
Multi-threaded: 2 files → 2 seconds (same as single-threaded!)

Conclusion: Multi-threading doesn't speed up I/O-bound tasks like file downloads.
It's still single-threaded underneath the hood.

"""
#space
#space
#space
"""
But for CPU-bound tasks, multi-threading is useless because:
Only one thread runs at a time anyway (GIL)
Threading just adds context-switching overhead
Use multiprocessing instead (separate processes, separate GILs)
"""
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Single-threaded
start = time.time()
cpu_task(100_000_000)
cpu_task(100_000_000)
elapsed = time.time() - start
print(f"Single-threaded: {elapsed:.1f}s")

# Multi-threaded
start = time.time()
t1 = threading.Thread(target=cpu_task, args=(100_000_000,))
t2 = threading.Thread(target=cpu_task, args=(100_000_000,))
t1.start()
t2.start()
t1.join()
t2.join()
elapsed = time.time() - start
print(f"Multi-threaded: {elapsed:.1f}s")