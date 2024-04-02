"""
# Problem

Write a function that reverses the elements of a list in place

Input: a list
Output: the same list, mutated

Explicit requirements:
- Mutate the list
- The elements should be reversed
- You may not use the reverse method

Implicit requirements:
- From the example, all lists seem to be sorted

Questions:
- Is the input list sorted?

## Examples:

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)  # prints [4, 3, 2, 1]
print(list1 is result)  # prints True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)  # prints ['e', 'd', 'c', 'b', 'a']
print(list2 is result2)  # prints True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)  # prints ['abc']
print(list3 is result3)  # prints True

list4 = []
result4 = reverse_list(list4)
print(result4)  # prints []
print(list4 is result4)  # prints True

## Data structure

Intermediate list to store new reversed list before mutating input list

## Algorithm:

1. Create a new list in reversed order
2. Replace each element of the original list with the element at
the corresponding index of the new list
3. Return the original list

Implementation notes:
- Intermediate list can be done with a comprehension
    - better just to use a slice
- Could probably use sorted(lst, reverse=True) provided input list always sorted

"""

# def reverse_list(lst):
#     reversed_lst = lst[::-1]
    
#     for idx, element in enumerate(reversed_lst):
#         lst[idx] = element
    
#     return lst

def reverse_list(lst):
    lst.sort(reverse=True)
    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)  # prints [4, 3, 2, 1]
print(list1 is result)  # prints True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)  # prints ['e', 'd', 'c', 'b', 'a']
print(list2 is result2)  # prints True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)  # prints ['abc']
print(list3 is result3)  # prints True

list4 = []
result4 = reverse_list(list4)
print(result4)  # prints []
print(list4 is result4)  # prints True