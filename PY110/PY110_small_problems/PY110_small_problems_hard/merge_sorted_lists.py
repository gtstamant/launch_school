"""
## Problem:

Write a function that takes two sorted lists
as arguments and returns a new list containing
all elements in sorted order

Input: two sorted lists
Output: a single, new sorted list

Explicit requirements:
- Do not sort the result list
- Do not mutate the original lists
- 

Implicit requirements:
- Sort in accordance with values
- Empty list not an issue

Questions:
- What happens when the lists are not the same length?
- Is the order sorted according to the values in the 
two lists or according to some other sort criterion?
- Can we assume that the arguments will have sortable
elements?
- What should we do with an empty list?

## Examples:
- see problem spec

## Data structure:
- list

## Algorithm:
- Initialize `sorted list` to an empty list
- Set two index pointers, `point1` and `point2` at 0
- Compare the element in lst1 at `point1` and lst2 at `point2`
    - If `point1` or `point2` is equal to the length of lst1 or lst 2
    respectively
        - Add all elements of the other list and return the result
    - if the element in lst1 is smaller
        - Add it to `sorted list`
        - Increment `point1` by 1
    - if the element in lst2 is smaller
        - Add it to `sorted list`
        - Increment `point2` by one
    - Repeat

"""
# def merge(lst1, lst2):
#     counter_1 = 0
#     counter_2 = 0
#     sorted_lst = []

#     while True:
#         if counter_1 == len(lst1):
#             sorted_lst.extend(lst2[counter_2:])
#             return sorted_lst

#         if counter_2 == len(lst2):
#             sorted_lst.extend(lst1[counter_1:])
#             return sorted_lst

#         current_1 = lst1[counter_1]
#         current_2 = lst2[counter_2]
#         if current_1 <= current_2:
#             sorted_lst.append(current_1)
#             counter_1 += 1
#         else:
#             sorted_lst.append(current_2)
#             counter_2 += 1

def merge(lst1, lst2):
    copy_1 = lst1[:]
    copy_2 = lst2[:]
    sorted_lst = []

    while copy_1 and copy_2:
        if copy_1[0] <= copy_2[0]:
            sorted_lst.append(copy_1.pop(0))
        else:
            sorted_lst.append(copy_2.pop(0))

    return sorted_lst + (copy_1 if not copy_2 else copy_2)


# print(merge([1, 5, 9], [2, 6, 8]))      # [1, 2, 5, 6, 8, 9]
# print(merge([1, 1, 3], [2, 2]))         # [1, 1, 2, 2, 3]
# print(merge([], [1, 4, 5]))             # [1, 4, 5]
# print(merge([1, 4, 5], []))             # [1, 4, 5]

