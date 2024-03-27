"""
## Product:

- Write a function that takes two lists as arguments
- It should return a new list
- Each element in the new list at a particular index
should be the product of the pair of numbers
at the same index in the two input lists

Input: pair of lists
Output: a list

Explicit requirements:
- Lists will contain the same # of elements

Implicit requirements:

Questions:
- What to do with an empty list?
- Might the lists have non-numeral elements?

## Example:

print(multiply_list(list1, list2) == [27, 50, 77])

## Data structure:
List

## Algorithm

1. Set 'results' to an empty list
2. Iterate through the input lists
- save the product of elements at a particular
index in list1 and list 2 in 'results'
3. Return 'results'

Implementation notes:

Can be done more easily with zip function,
I think also some array?

"""

# def multiply_list(list1, list2):
#     results = []
#     for idx in range(len(list1)):
#         results.append(list1[idx] * list2[idx])
#     return results

# def multiply_list(list1, list2):
#     return [item1 * item2 
#             for (item1, item2) 
#             in zip(list1, list2)]

# Trying to see if I can do it recursively

def multiply_list(list1, list2):
    if len(list1) == 1:
        return [list1[0] * list2[0]]
    return [list1[0] * list2[0]] + multiply_list(list1[1:], list2[1:])

list1 = [3, 5, 7]
list2 = [9, 10, 11]

print(multiply_list(list1, list2) == [27, 50, 77])  # True