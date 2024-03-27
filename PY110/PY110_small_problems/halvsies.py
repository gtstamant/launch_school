"""
## Problem

Take a list argument and return a list that contains two sublists
each of which contains half the elements from the initial list

Input: a list
Output: a nested list

Explicit requirements:
- Each sublist should contain half of the initial elements
- If there is an odd number of elements, the extra one goes in the first
sublist

Implicit requirements:
- An empty list argument should return a list containing
two empty lists
- An argument list with one element should return a list
containing one element list and an empty list

Questions:
- Should the elements maintain their original order?

## Examples

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

## Data structure

Lists, perhaps some intermediary ones as well

## Algorithim

1. Determine length of list
    - if 0, return list containing two empty lists
    - if 1, return list containing original list and empty list
2. Divide length in 2 to get 'result' 
    - if divisible by 2
        - sublist length 'sub len 1' and 'sub len 2' set to 'result'
    - if not divisible by 2
        - set 'sub len 1' to smallest integer greater than 'result'
        - set 'sub len 2' to largest integer smaller than 'result'
3. Return a list that contains two lists
    - the first contains the elements up to 'sub len 1' taken from
    initial list
    - the second contains the elements up to 'sub len 2' taken from
    initial list

Implementation notes:
- Need to account for empty list, list of one element?
- In all other cases can generate sublists by slicing
    - floats cannot index!

"""

def halvsies(lst):
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
