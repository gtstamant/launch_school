"""
## Problem:

Write a function that takes a list argument and sorts
it using a merge sort algorithm

Explicit requirements:
- Take one argument, a list
- Recursively reduce the list to nested sublists of one element
- Sort adjacent sublists and build the list back up

Implicit requirements:
- Do not mutate the original list

Questions:
- Can we assume valid inputs?

## Examples:
- See problem spec

## Data structure:
- Nested lists

## Algorithm:

- Split the list in half
    - Place the resulting halves in a list
        - If the elements have more than one element
            - Repeat from the top
    - If the elements are lists with one element
        - merge with sorted list subprocess

"""
def merge(lst1, lst2):
    copy1 = lst1[:]
    copy2 = lst2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))
    
    return result + (copy1 if not copy2 else copy2)

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    midpoint = len(lst) // 2
    return merge(merge_sort(lst[:midpoint]), 
                 merge_sort(lst[midpoint:]),)

print(merge_sort([9, 5, 7, 1]))           # [1, 5, 7, 9]
print(merge_sort([5, 3]))                 # [3, 5]
print(merge_sort([6, 2, 7, 1, 4]))        # [1, 2, 4, 6, 7]

print(merge_sort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']))
# ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

print(merge_sort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]))
# [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]