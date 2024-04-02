"""
## Problem:

Write a function that takes to integer arguments
The first argument is a `count` and the second is a starting point
The function should return a list that contains `count` number of elements
Each element should be a multiple of the starting number

## Examples:

print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []

## Data structure
- A list

## Algorithm

1. Initialize `sequence` to an empty list
2. For each number between 1 and `count`
    - Append `start` * number to `sequence`
3. Reutrn the list

Implementaiton notes:
- Remember the 0 condition, if `count` is 0, return an empty list
- Can iterate over a range object from 1 - count + 1
- Can probably use a comprehension

"""

def sequence(count, start):
    return [start * num for num in range(1, count + 1)]

print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []