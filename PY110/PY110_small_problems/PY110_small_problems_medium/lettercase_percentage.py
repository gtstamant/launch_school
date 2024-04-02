"""
## Problem:

Write a function that takes a string and returns
an object containing three properties:
- Percentage of chars in string that are lowercase
- Percentage of chars in string that are uppercase
- Percentage of chars in string that are neither

Input: a string
Output: a dictionary containing abovementioned data

Explicit requirements:
- Expect a string argument
- Argument will always include at least one char

Implicit requirements:
- Format as follows
{ 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }
- Spaces count as chars

Questions:
- Usual about need to do input validation
- Do spaces count as chars?

## Examples:

print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }
Total: 10 (counting space as 1)
Lower: 5
Upper: 1
Num, space = 4

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }

## Data structure:
- dictionary

## Algorithm:

- Initialize `type count` as an empty dictionary
- Cycle through each character of the string
    - Test whether the character is upper, lower, or neither
    - Check whether type exists as key in `type count`
        - If so, increment value associated with type
        - If not, add `type` as a key and set associated value to 1
- Return dict with modified values

"""
import re

def letter_percentages(s):
    
    def percentages(pattern):
        matches = re.findall(pattern, s)
        return f'{(len(matches) / len(s)) * 100:.2f}'
    
    return{'uppercase'  : percentages(r'[A-Z]'),
           'lowercase'  : percentages(r'[a-z]'),
           'neither'    : percentages(r'[^A-Za-z]')}


# def letter_percentages(s):
#     type_count = {'uppercase': 0, 'lowercase': 0, 'neither': 0}

#     for char in s:
#         if char.isupper():
#             type_count['uppercase'] += 1
#         elif char.islower():
#             type_count['lowercase'] += 1
#         else:
#             type_count['neither'] += 1
    
#     return {key: f'{((value / len(s)) * 100):.2f}' for key, value
#             in type_count.items()}

# print(letter_percentages('abCdef 123'))
# # { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

# print(letter_percentages('AbCd +Ef'))
# # { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

# print(letter_percentages('123'))
# # { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }


if re.search(r'[0-9A-Ja-j]', 'cap'):
    print('Found')

else:
    print('Not found')