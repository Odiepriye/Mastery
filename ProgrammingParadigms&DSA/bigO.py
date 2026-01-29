"""
Big O Notation is a way to measure the time complexity of an algorithm.
It shows how an algorithm's performance scales with input size
Big O measures WORST-CASE time complexity as input size (n) approaches infinity.
It shows how the time complexity of an algorithm increases as the input size increases.
"""

""" 
O(1) - Constant time - The time complexity is the same regardless of the input size.
""" 
def get_first_element(lst):
    return lst[0]

# Why? Hash tables use memory addresses for instant lookup
# Dictionary/Set operations are O(1)
d = {'key': 'value'}
value = d['key']  # O(1) - Direct hash table lookup
d['new_key'] = 'new_value'  # O(1) - Insert

s = {1, 2, 3, 4, 5}
if 3 in s:  # O(1) - Set membership check
    pass


""" 
O(n) - Linear time - The time complexity increases linearly with the input size.
""" 
def get_index_of_element(x : int, lst : list[int]) -> int:
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1
# List iteration is O(n)
for item in [1, 2, 3, 4, 5]:  # O(n) - Visit each item once
    pass

# Dictionary iteration is O(n)
for key in {'a': 1, 'b': 2, 'c': 3}:  # O(n) - Visit each key once
    pass


""" 
O(n^2) - Quadratic time - The time complexity increases quadratically with the input size.
E.g.
TWO nested loops 
Compare every element in 2 iterables
String concatenation in loop
""" 
def find_equal_elements(lst1 : list[int], lst2 : list[int]) -> list[int]:
    for element in lst1:
        if element in lst2:
            return element
    return None

# STRING CONCATENATION TRAP - O(n²)!
print("String concatenation in loop (SLOW):")
result = ""
for char in "hello":
    result += char  # Each += creates a NEW string (immutable)
# Iteration 1: "h" (1 op)
# Iteration 2: "he" (2 ops - copy "h" + add "e")
# Iteration 3: "hel" (3 ops)
# Total: 1+2+3+4+5 = 15 ops = O(n²)!

# BETTER APPROACH: Use join() - O(n)
result = "".join("hello")  # O(n) - allocate once, fill once


""" 
O(log n) - Logarithmic time - The time complexity increases logarithmically with the input size.
This algorithm that halves the space on every iteration and only works on sorted lists.
In this example Binary Search example x must be found in a sorted list lst.
""" 
# Binary search is O(log n)
def binary_search(x: int, lst: list[int]) -> int:
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1  # Discard left half
        else:
            right = mid - 1  # Discard right half
    return -1

# Halving pattern = log n
import math
for n in [100, 1000, 10000, 1000000]:
    ops = math.log2(n)
    print(f"  {n:>7} items: ~{ops:.0f} operations")
print()


""" 
O(n log n) - Log-linear time - The time complexity increases logarithmically with the input size and linearly with the input size.
This is best described as a search/sort algorithm that halves the space on every iteration and then sorts the result.
In Merge Sort example the list is split into 2 halves and then sorted and merged.
""" 
def merge_sort(lst : list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge_sort(left, right)

""" 
O(2^n) - Exponential time - The time complexity increases exponentially with the input size.
This is best described as a search/sort algorithm that doubles the space on every iteration.
In Fibonacci example the number of calls to the function increases exponentially with the input size.
""" 
def fibonacci(n : int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

""" 
O(n!) - Factorial time - The time complexity increases factorially with the input size.
This is best described as a search/sort algorithm that increases the space by a factorial amount on every iteration.
In Permutations example the number of permutations increases factorially with the input size.
""" 
def permutations(lst : list[int]) -> list[list[int]]:
    if len(lst) <= 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        for perm in permutations(lst[:i] + lst[i+1:]):
            result.append([lst[i]] + perm)
    return result