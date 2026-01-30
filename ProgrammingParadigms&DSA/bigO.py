"""
Big O Notation is a way to measure the time complexity of an algorithm.
It shows how an algorithm's performance scales with input size
Big O measures WORST-CASE time complexity as input size (n) approaches infinity.
It shows how the time complexity of an algorithm increases as the input size increases.
"""

""" 
O(1) - Constant time: 
The time complexity is the same regardless of the input size.
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
O(n) - Linear time: 
The time complexity increases linearly with the input size.
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
O(n^2) - Quadratic time: 
The time complexity increases quadratically with the input size.
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
O(log n) - Logarithmic time:
The time complexity increases logarithmically with the input size.
This is a search algorithm that halves the space on every iteration and only works on sorted lists.
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

# Suppose lst has 16 elements:
# Iteration 1: 16 elements → check middle → discard half → 8 left
# Iteration 2:  8 elements → check middle → discard half → 4 left
# Iteration 3:  4 elements → check middle → discard half → 2 left
# Iteration 4:  2 elements → check middle → discard half → 1 left
# Iteration 5:  1 element → found or not

# Halving pattern = log n
import math
for n in [100, 1000, 10000, 1000000]:
    ops = math.log2(n)
    print(f"  {n:>7} items: ~{ops:.0f} operations")
print()


""" 
O(n log n) - Log-linear time: 
The time complexity grows linearly with the number of elements (n)
and logarithmically with the number of times the input is divided (log n).

This occurs in divide-and-conquer algorithms.
The input is repeatedly split in half (log n levels),
and at each level all n elements are processed.
""" 
# Merge Sort — O(n log n)
# Idea:
# 1. DIVIDE: Recursively split the list in half (log n levels)
# 2. CONQUER: Merge sorted halves back together (n work per level)
# Total time = n × log n

def merge_sort(lst: list[int]) -> list[int]:
    # Base case:
    # A list of length 0 or 1 is already sorted
    # No more splitting needed
    if len(lst) <= 1:
        return lst

    # Find the middle index
    # This splits the list roughly in half
    mid = len(lst) // 2

    # Recursively sort the left half
    # This keeps dividing the list until size == 1
    left = merge_sort(lst[:mid])

    # Recursively sort the right half
    right = merge_sort(lst[mid:])

    # Merge the two sorted halves into one sorted list
    # This merge step touches each element once → O(n)
    return merge(left, right)


def merge(left, right):
    # Result list that will contain the merged, sorted elements
    result = []

    # Pointers for left and right lists
    i = 0  # index for left
    j = 0  # index for right

    # Compare elements from both lists
    # Continue until one list is exhausted
    while i < len(left) and j < len(right):
        # Compare current elements
        if left[i] <= right[j]:
            # Append the smaller element from left
            result.append(left[i])
            i += 1  # move left pointer
        else:
            # Append the smaller element from right
            result.append(right[j])
            j += 1  # move right pointer

    # One of the lists may still have elements left
    # These elements are already sorted
    # Append them directly (no comparisons needed)
    result.extend(left[i:])
    result.extend(right[j:])

    # Return the merged, sorted list
    return result

# BIG-O EXPLANATION (STEP-BY-STEP): 
# 
# 1. DIVIDING PHASE:
#    Each recursive call splits the list in half
#    Number of split levels = log₂(n)
#
# 2. MERGING PHASE:
#    At each level, ALL n elements are merged once
#    Merge cost per level = O(n)
#
# 3. TOTAL WORK:
#    O(n) work × O(log n) levels
#    = O(n log n)
#
# Merge sort is:
# - Faster than O(n²) algorithms (like bubble sort)
# - Stable
# - Predictable performance
# - Uses extra memory for merging


""" 
O(2^n) - Exponential time: 
The time complexity increases exponentially with the input size.
This is best described as a search/sort algorithm that doubles the space on every iteration.
In Fibonacci example the number of calls to the function increases exponentially with the input size.
""" 
def fibonacci(n : int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)#2 recursive calls on each iteration

# Recursive fibonacci (inefficient)
# fib(5): 15 function calls
# fib(10): 177 function calls
# fib(30): 2,178,309 function calls (!)
# Doubles with each increase in n

# Why? Each call branches into 2 calls (exponential tree)


""" 
O(n!) - Factorial time: 
The time complexity increases factorially with the input size.
This is best described as a search/sort algorithm that increases the space by a factorial amount on every iteration.
In Permutations example the number of permutations increases factorially with the input size.
""" 

# Generate all permutations
def permutations(lst: list[int]) -> list[list[int]]:
    if len(lst) <= 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        for perm in permutations(lst[:i] + lst[i+1:]):
            result.append([lst[i]] + perm)
    return result

# Generate all permutations:
# 5 items: 120 permutations (5!)
# 10 items: 3,628,800 permutations (10!)
# 15 items: 1.3 TRILLION permutations (15!)


"""
=== COMMON DATA STRUCTURE OPERATIONS ===

LIST OPERATIONS:
  lst[i]              O(1)  - Direct index access
  lst.append(x)       O(1)  - Add to end (amortized)
  lst.insert(0, x)    O(n)  - Shift all items
  lst.remove(x)       O(n)  - Search + shift
  x in lst            O(n)  - Linear search
  lst.sort()          O(n log n)  - Efficient sorting

DICTIONARY/SET OPERATIONS:
  d[key]              O(1)  - Hash table lookup
  d[key] = value      O(1)  - Hash table insert
  key in d            O(1)  - Hash lookup
  d.keys()            O(n)  - Copy all keys
  dict(other_dict)    O(n)  - Copy all items

STRING OPERATIONS:
  s[i]                O(1)  - Index access
  s + s2              O(n)  - Creates new string (copies both)
  s.join(list)        O(n)  - One allocation + fill
  s in s2             O(n)  - Search substring
  s.split()           O(n)  - Create new strings

SORTING:
  sorted(list)        O(n log n)  - Efficient (uses Timsort)
  list.sort()         O(n log n)  - In-place sorting
  bubble_sort(list)   O(n²)  - Inefficient


For n = 100,000 items:

O(1)        - 1 operation           ✓ Instant
O(log n)    - ~17 operations        ✓ Instant
O(n)        - 100,000 ops           ✓ Fast
O(n log n)  - ~1.7 million ops      ✓ Acceptable
O(n²)       - 10 billion ops        ✗ SLOW (seconds/minutes)
O(2^n)      - 2^100k ops            ✗ IMPOSSIBLE
O(n!)       - 100k! ops             ✗ IMPOSSIBLE
"""