"""
## Problem:

Define a function that takes two list arguments and
returns a set that contains the union of those two lists

Input: two lists
Output: a set

Explicit rules:
- 

Implicit rules:
- No duplicate elements in output

Questions:
- Will lists ever contain non-hashable items?
- Can we use python's set constructor?
- Can we use a set comprehension?

## Examples:

union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9})

## Data structure:

Set

## Algorithm:

1. Add each item from the two lists to a new data structure
2. Search and remove duplicates
3. Return data structure

Implementation notes:

This is easily accomplished with built-in functions.
We could just extend the list and convert it to a set.
We could also create a set through a comprehension that
runs over both lists.

"""

# def union(list1, list2):
#     return set(list1 + list2)


# Nested comprehension practice

def union(list1, list2):
    return {item for sublist in [list1, list2]
            for item in sublist}


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True