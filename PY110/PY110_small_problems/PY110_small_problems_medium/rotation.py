"""
## Problem:

Write a function that takes a list as an argument and 
returns a new list. The new list should move the first 
element of the original list to the end of the new list

Input: a list
Output: a new list

Explicit requirements:
- Must return a new list
- Do not mutate the original list
- Move the first element in the `input` list to
the end of the `return` list
- If input is not a list, return none
- If input is an empty list, return an empty list

Implicit requirements:

Questions:

## Examples:

See examples given on problem page

## Data structure:

List

## Algorithm:
- Create a copy of the original list
- Move the first element to the final position

Implementation notes:
- Easiest to concatenate two partial slices
- Don't forget input validation and empty lists
- Don'f forget single element lists

"""

def rotate_list(lst):
    if not type(lst) is list:
        return None
    try:
        return lst[1:] + [lst[0]]
    except IndexError:
        return lst
    
print(rotate_list([7, 3, 5, 2, 9, 1]))           # [3, 5, 2, 9, 1, 7]
print(rotate_list(['a', 'b', 'c']))              # ['b', 'c', 'a']
print(rotate_list(['a']))                        # ['a']
print(rotate_list([1, 'a', 3, 'c']))             # ['a', 3, 'c', 1]
print(rotate_list([{'a': 2}, [1, 2], 3]))       # [[1, 2], 3, {'a': 2}]
print(rotate_list([]))                           # []

# return `None` if the argument is not a list
print(rotate_list(None))                         # None
print(rotate_list(1))                            # None

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst))                    # [2, 3, 4, 1]
print(lst)                                # [1, 2, 3, 4]