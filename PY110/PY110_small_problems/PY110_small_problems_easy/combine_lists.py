"""
## Problem

Take two lists and return a new list that takes elements
from each initial list in alteration

Input: two lists
Output: a single list

Explicit requirements:
- Both lists will have the same number of elements
- Take one item from the first list, then one from the second, repeat
- No empty lists

Implicit requirements:
- Elements should retain their order as inputted into new list

## Data structure

A list

Algorithim:

1. Set 'result' to a new list
2. Add items until all items added
    - add an item from list 1
    - add an item from list 2
    - check if at end
3. Return list

Implementation notes:

Could accomplish with nested comprehension
that cycles through the two lists on the basis of an index?

"""

# def interleave(list1, list2):
#     result = []

#     for index in range(len(list1)):
#         result.append(list1[index])
#         result.append(list2[index])
    
#     return result

# just to see if I could do with nested comprehensions
# def interleave(list1, list2):
#     result = [
#         item for subtup in
#         [(list1[index], list2[index])        
#         for index in range(len(list1))
#         ]
#         for item in subtup]
    
#     return result

# def interleave(list1, list2):
#     result = []
    
#     for index in range(len(list1)):
#         result.extend([list1[index], list2[index]])

#     return result

def interleave(list1, list2):
    return [element for tuple in zip(list1, list2)
            for element in tuple]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True