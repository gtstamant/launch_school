"""
## Problem:

Write a function that sorts a list using a bubble sort algorithm

Input: a list
Output: a sorted list

Explicit requirements:
- The sorting should be done in-place

## Examples:
- See problem spec

## Data structure:
- a list

## Algorithm:

1. Take a `list` as an argument
2. Set `move` equal to False
    - Set the element at index 0 as `current`
    - Compare `current` to the next element
    - if `current` is larger
        - Swap their positions
        - set `move` equal to True
        - Return to comparison step
    - if `current` is smaller
        - Set `current` equal to the next element
        - Return to comparison step
    - Once final element is reached
        - If `move` is equal to false
            - return list
        - If `move` is equal to true
            - Set `move` equal to false
            
"""

def bubble_sort(lst):
    swap = False
    length = len(lst)
    while True:
        for idx in range(1, length):
            if lst[idx - 1] > lst[idx]:
                lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
                swap = True
        
        if swap == False:
            return lst
        
        swap = False
        length -= 1 # Optimization

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)    # [3, 5]

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)    # [1, 2, 4, 6, 7]

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3)    # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]