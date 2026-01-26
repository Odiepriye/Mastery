"""
Memory Management in Python

Python uses reference counting and garbage collection for memory management.

- Python's Objects are deleted when the reference count reaches 0
"""

import sys
import gc

print("=== REFERENCE COUNTING ===\n")

x = [1, 2, 3]      # refcount = 1
print(f"x = [1,2,3], refcount = {sys.getrefcount(x)}")

y = x              # refcount = 2 (y also points to it)
print(f"After y = x, refcount = {sys.getrefcount(x)}")

z = x              # refcount = 3 (z also points to it)
print(f"After z = x, refcount = {sys.getrefcount(x)}")

del y              # refcount = 2 (y is deleted)
print(f"After del y, refcount = {sys.getrefcount(x)}")

del z              # refcount = 1 (z is deleted)
print(f"After del z, refcount = {sys.getrefcount(x)}")

del x              # refcount = 0 (x is deleted immediately!)
print("After del x, object deleted (refcount = 0)")


print("\n=== CIRCULAR REFERENCES PROBLEM ===\n")

"""
Circular references would leak WITHOUT the GC, but...
Python's Garbage Collector detects and frees circular references

Python's GC uses a mark-and-sweep algorithm:

- Mark phase: Start from "root" objects (global variables, stack frames)
  Follow pointers: "Is this object reachable from root objects?"

- Sweep phase: Any object NOT marked is unreachable
  Even if it has a refcount > 0 (because it's in a cycle)
  Delete it!
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

print("Creating circular reference...")
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference!

print(f"node1 refcount: {sys.getrefcount(node1)}")
print(f"node2 refcount: {sys.getrefcount(node2)}")

print("\nDeleting references...")
del node1
del node2

print("Both deleted by Garbage Collector!")
print("(GC detected: node1 → node2 → node1, unreachable from root)")


print("\n=== GARBAGE COLLECTION ===\n")

print("GC runs periodically, but you can trigger it manually:")
print(f"Objects freed this collection: {gc.collect()}")

print("\nYou can also check GC thresholds:")
print(f"GC thresholds: {gc.get_threshold()}")
print("(Collect after N allocations)")


print("\n=== KEY TAKEAWAYS ===\n")
print("✓ Reference counting: Primary mechanism (immediate)")
print("✓ GC: Secondary mechanism (handles cycles)")
print("✓ Most objects freed immediately when refcount = 0")
print("✓ Circular references freed by GC mark-and-sweep")
print("✓ GC runs periodically (can force with gc.collect())")
print("✓ You rarely need to think about this in practice")