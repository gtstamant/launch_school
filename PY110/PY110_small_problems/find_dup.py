"""
## Problem

Provided with an unordered list as an argument. Determine which value
in that list occurs exactly twice.

Input: a list
Output: an int

Explicit requirements:
- Unordered list argument
- Only one value occurs twice, all others once

Implicit requirements:
- Seems from examples that all items are ints

Questions:
- Is every item an int?
- How should we handle an empty list? (I guess not possible?)

## Examples:

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True

## Data structure

Perhaps a dict to keep track of the number of times a value appears?

## Algorithim

1. Set 'occurences' to empty associative data structure
2. Cycle through every number in list
    - Check if number in data structure
        - if not, add with count 1
        - if so, return number   

## Implementation notes

Seems like a good case for a dictionary; could use
comprehension but maybe can't optimize by halting when
dup found?

Could also successively build a set and check whether consecutive num
in set?

"""

# def find_dup(lst):
#     occurences = {}

#     for num in lst:
#         if occurences.get(num) == None:
#             occurences[num] = 1
#         else:
#             return num


# def find_dup(lst):
#     considered_nums = set()

#     for num in lst:
#         if num in considered_nums:
#             return num
#         considered_nums.add(num)

# def find_dup(lst):
#     return sum(lst) - sum(set(lst))

# def find_dup(lst):
#     for num in lst:
#         if lst.count(num) == 2:
#             return num

def find_dup(lst):
    return [num for num in lst if lst.count(num) == 2][0]


print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True