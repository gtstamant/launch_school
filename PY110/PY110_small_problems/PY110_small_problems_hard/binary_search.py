"""
## Problem:

Write a `binary search` function that takes
a list and a search item as arguments and 
returns the index of the search item if found
or -1 otherwise

Input: a list, a search item
Output: the index of the item, -1 if not present

Explicit requirements:
- See above

Implicit requirements
- Must be able to search different types of items
- List argument will be sorted

## Examples:
- See problem spec

## Data structure
- no need

## Algorithm

- Look at the middle item of a list
- If the list has length of 1
    - Return -1
- If it is the `search term`
        - Return the index
- If it is not the search term
    - If the middle item is bigger than the search term
        - Search the half of the list prior to the middle item
    - Otherwise
        - Search the half of the list bigger than the middle item

## Non-recursive solution:

## Algorithm:

- Set `idx` to half the length of the list
- Check if the element indexed at `idx`, called `guess`, is equal to the `target`
- If so 
    - return `guess`
-If not
    - Check if element is greater than `guess`
    - If so
        - Make idx the end element
        - Beginning of the list the beginning
        - Check at middle
    - If not:
        - Switch idx to half of the length between the 


"""

# def binary_search(lst, target):
#     beginning = 0
#     end = len(lst) - 1

#     while beginning <= end:
#         guess = (beginning + end) // 2

#         if lst[guess] == target:
#             return guess
#         if lst[guess] > target:
#             end = guess - 1
#         elif lst[guess] < target:
#             beginning = guess + 1

#     return -1
        
    


def binary_search(lst, target, idx_shift=0):
    if len(lst) == 1:
        return idx_shift if lst[0] == target else -1

    midpoint = len(lst) // 2
    guess = lst[midpoint]

    if guess == target:
        return midpoint + idx_shift
    if guess > target:
        return binary_search(lst[:midpoint], target)
    if guess < target:
        return binary_search(lst[midpoint + 1:], target, idx_shift + midpoint + 1)

businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
# print(binary_search(businesses, 'Pizzeria') == 7)
# print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)