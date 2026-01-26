"""
BYTECODE: Python's Internal Execution Model

1. How Python Runs:
- Python doesn't run directly from source code
- Code is converted to .pyc (bytecode) and executed by Python Virtual Machine (PVM)
- First run creates .pyc in __pycache__ dir
- Subsequent runs detect changes and recompile
- Bytecode is intermediate format between source and machine code

2. How Bytecode Works:
- Each line of Python code is converted to one or more bytecode instructions
- Instructions are executed by PVM
- Each bytecode instruction runs once per function call
"""

# Let's see actual bytecode
# import dis

# def add(x, y):
#     return x + y

# print("=== BYTECODE FOR add(x, y) ===")
# dis.dis(add)
# print("====== END OF BYTECODE ======")

# print("\n=== BYTECODE FOR calculate(a, b, c) ===")
# def calculate(a, b, c):
#     result = a + b
#     result = result * c
#     return result

# dis.dis(calculate)
# print("====== END OF BYTECODE ======")

"""
STACK FRAMES: Where Local Variables Live

A stack frame stores:
- Local variables
- Function arguments  
- Code being executed
- Return address (where to go after function finishes)

When a function calls another function, a new frame is pushed on the stack.
When a function returns, its frame is popped off the stack.
"""

print("\n=== STACK FRAMES IN ACTION ===\n")

import inspect

def show_stack():
    """Shows the current call stack"""
    print("Current call stack:")
    for frame_info in inspect.stack():
        print(f"  {frame_info.function}() at line {frame_info.lineno}")

def outer(x):
    print(f"In outer(x={x})")
    y = 10
    print(f"  Set y = {y}")
    print("  About to call inner()...")
    result = inner(y)
    print(f"  inner() returned {result}")
    return result

def inner(z):
    print(f"In inner(z={z})")
    show_stack()  # Show frames while inner() is executing
    w = 20
    print(f"  Set w = {w}")
    print(f"  Returning {z + w}")
    return z + w

print("Calling outer(5):")
outer(5)
"""
┌─────────────────────┐
│  Frame: inner()     │  ← Currently executing
│  z = 20             │
│  w = 20             │
├─────────────────────┤
│  Frame: outer()     │  ← Waiting for inner() to finish
│  x = 5              │
│  y = 10             │
├─────────────────────┤
│  Frame: main        │  ← Python's entry point
└─────────────────────┘

Each function gets its own frame. When a function returns, its frame is removed from the stack.
"""
