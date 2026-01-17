"""
Generators are functions that can pause or resume their execution
When a generator function is called it returns a generator object which is an iterator
The function is not executed yet and is only executed when iterated over

It fixes a core  memoemory/computation issue of iterators,
where the entire iterable is loaded into memory at once"""

# # BAD: Loads everything into memory at once
# from multiprocessing import process


# def get_all_numbers(n):
#     result = []
#     for i in range(n):
#         result.append(i)
#     return result  # Returns a list with 1,000,000 items!

# numbers = get_all_numbers(1000000)
# # Your computer just allocated memory for 1 million items
# for num in numbers:
#     print(num)

# # GOOD: Produces values one at a time, on demand
# def get_all_numbers_generator(n):
#     for i in range(n):
#         yield i  # Pause here, return i, then resume later

# numbers = get_all_numbers_generator(1000000)
# # Nothing happens yet! No memory allocated.
# for num in numbers:
#     print(num)  # Now it produces values ONE AT A TIME

# # BAD: Loads entire file into memory
# def read_file_bad(filename):
#     with open(filename) as f:
#         return f.readlines()  # All lines at once!

# lines = read_file_bad('huge_file.txt')  # 1GB file = uses 1GB RAM
# for line in lines:
#     process(line)


# # GOOD: Reads line by line, on demand
# def read_file_good(filename):
#     with open(filename) as f:
#         for line in f:
#             yield line  # One line at a time!

# lines = read_file_good('huge_file.txt')  # No memory used yet
# for line in lines:
#     process(line)  # Only 1 line in memory at a time

"""
yield vs return
RETURN: Runs once, gives one value, function exits
YIELD: Runs multiple times, gives multiple values, pauses between

"""     
# RETURN: Runs once, gives one value, function exits
def with_return():
    return 1
    return 2  # Never reaches here
    return 3  # Never reaches here

result = with_return()
print(result)  # 1


# YIELD: Runs multiple times, gives multiple values, pauses between
def with_yield():
    yield 1
    yield 2
    yield 3

gen = with_yield()
print(next(gen))  # 1 (pauses after first yield)
print(next(gen))  # 2 (resumes, pauses after second yield)
print(next(gen))  # 3 (resumes, pauses after third yield)

"""
Generator pipelines
The real beauty of generators is in pipelines
you can chain multiple generators together to create a pipeline
each generator processes the data and passes it to the next generator
this way you can process large amounts of data without loading it all into memory
"""
def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line

def filter_comments(lines):
    for line in lines:
        if not line.startswith('#'):
            yield line

def uppercase(lines):
    for line in lines:
        yield line.upper()

# Pipeline: read → filter → uppercase
pipeline = uppercase(filter_comments(read_file('data.txt')))

for processed_line in pipeline:
    print(processed_line)

# Only 1 line in memory at a time!  

"""
iterators and generators are the same thing
an iterator is a class that implements the __iter__ and __next__ methods
a generator is a function that uses the yield keyword to pause and resume execution
they both implement the iterator protocol and return an iterator object which means they can be used in a for loop
but generators are more convenient to use since they are functions and can be paused and resumed

Under the hood a generator automatically creates:
an object with __iter__()
a __next__() method
saves local state (a, b, execution position)
When you write an iterator class, you must do all of that yourself.
"""
# generator fibonacci example
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Iterator example
class MyIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
        
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


"""
WHEN TO USE GENERATORS VS ITERATORS

DEFAULT: Use Generators 99% of the time
ONLY: Use Iterators when generators don't fit

GENERATORS: Function-based, simpler code
- Automatically handle __iter__ and __next__
- State is implicit (local variables)
- Code is readable and concise
- Used once (exhausted after iteration)

ITERATORS: Class-based, more control
- Explicit __iter__ and __next__ methods
- State is explicit (instance variables)
- Can have multiple methods and properties
- Can be reset and iterated multiple times

DECISION TREE:
1. Need to iterate SAME object multiple times? → ITERATOR
2. Need complex state with multiple methods? → ITERATOR
3. Need to expose properties/stats during iteration? → ITERATOR
4. Need custom iteration protocol control? → ITERATOR
5. Otherwise? → GENERATOR (default)
"""

# SCENARIO 1: Simple Sequence → GENERATOR
print("=== SCENARIO 1: Simple Sequence ===")
def simple_gen():
    for i in range(3):
        yield i

for x in simple_gen():
    print(f"Gen: {x}")


# SCENARIO 2: Reusable Iterator (iterate multiple times)
print("\n=== SCENARIO 2: Iterate Multiple Times ===")

# Generator FAILS:
print("Generator (exhausts after first iteration):")
def numbers_gen():
    for i in range(3):
        yield i

gen = numbers_gen()
print("Iteration 1:", list(gen))
print("Iteration 2:", list(gen))  # Empty!

# Iterator WORKS:
print("\nIterator (can iterate multiple times):")
class NumbersIterator:
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current >= 3:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

it = NumbersIterator()
print("Iteration 1:", list(it))
print("Iteration 2:", list(it))  # Works!


# SCENARIO 3: Complex State with Methods
print("\n=== SCENARIO 3: Complex State with Methods ===")

class DataProcessor:
    """Iterator that tracks stats during iteration"""
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.items_processed = 0
    
    def __iter__(self):
        self.index = 0
        self.items_processed = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        self.items_processed += 1
        return result
    
    def get_progress(self):
        """Extra method! Generators can't have this"""
        return f"Processed {self.items_processed}/{len(self.data)}"

processor = DataProcessor([1, 2, 3, 4, 5])
for item in processor:
    print(f"Item: {item}, Progress: {processor.get_progress()}")


# SCENARIO 4: Stateful Iteration with Reset
print("\n=== SCENARIO 4: Stateful Sliding Window ===")

class SlidingWindow:
    """Iterator for sliding window over a sequence"""
    def __init__(self, sequence, window_size):
        self.sequence = sequence
        self.window_size = window_size
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index + self.window_size > len(self.sequence):
            raise StopIteration
        window = self.sequence[self.index:self.index + self.window_size]
        self.index += 1
        return window
    
    def peek_next(self):
        """Extra method: preview what's coming next"""
        if self.index + self.window_size <= len(self.sequence):
            return self.sequence[self.index:self.index + self.window_size]
        return None

window = SlidingWindow([1, 2, 3, 4, 5], 3)
for w in window:
    print(f"Window: {w}, Next: {window.peek_next()}")


# COMPARISON TABLE
"""
FEATURE                 | GENERATOR | ITERATOR
Simple to write        | YES       | NO (boilerplate)
Can iterate twice      | NO        | YES
Can have methods       | NO        | YES
Can track stats        | AWKWARD   | NATURAL
Memory usage           | SAME      | SAME
Performance           | SAME      | SAME

REAL-WORLD RULE:
- Parse a file once? GENERATOR
- Parse a file, reuse iterator? ITERATOR
- Transform data lazily? GENERATOR
- Complex stateful processing? ITERATOR
- Most cases? GENERATOR (default!)
"""


# WHEN GENERATORS ARE ENOUGH (USE THESE!)
"""
✅ Streaming data through pipelines
✅ Processing large files
✅ One-time iterations
✅ Simple transformations
✅ Infinite sequences (range, fibonacci)
✅ Lazy evaluation of expressions
"""

# WHEN ITERATORS ARE NEEDED
"""
✅ Reusable iteration (iterate same object multiple times)
✅ Complex stateful processing
✅ Need to expose stats/methods
✅ Need iteration control (peek, reset, etc.)
✅ Object-oriented design (is-a Sequence type)
"""

