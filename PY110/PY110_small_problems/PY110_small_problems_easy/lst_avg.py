"""
## Problem:

Write a function that takes a list of integers
and returns the avg of that list. The avg should
be rounded down to the integer component of the
average (that is, exclude the decimal component)

Input: a list
Output: an int

Explicit requirements:
- List will never be empty
- All elements are positive integers

Implicit requirements:

Questions:
- Quite clear

## Examples

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

Data structure:

A list

Algorithm:

1. Add up all the elements in the 'input' list
2. Divide them by the number of elements
3. Throw away the decimal portion of the result
4. Return the result

Implementation notes:
- built in sum function to compute sum of all elements
- len() to compute num elements
- use floor division to throw away decimal

"""

def average(lst):
    return sum(lst) // len(lst)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True