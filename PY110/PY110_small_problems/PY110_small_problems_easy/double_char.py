"""
# Problem:

Write a function that
- Takes a string as an argument
- Doubles every character within the string
- returns the result as a new string

Input: a string
Output: a string

Explicit requirements:

Implicit requirements:
- Empty string should return an empty string

Questions:
- How to handle an empty string

## Examples:

print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""

## Data structure

Not sure we need one

## Algorithim:

Mental model:

Start by setting an empty string to contain the result.
Cycle through each of the characters in the input string,
and, for each character, append two instances of that
character to the result string.

Once all characters have been considered, return the result.

Algorithm:

1. Set 'result' to empty string
2. For each character in 'input'
- Add two of that character to 'result
3. Return result

"""

# def repeater(input_str):
#     result_str = ''

#     for char in input_str:
#         result_str += char * 2
    
#     return result_str

def repeater(input_str):
    return ''.join([char * 2 for char in input_str])

print(repeater('Hello') == "HHeelllloo")
print(repeater('Good job!') == "GGoooodd  jjoobb!!")
print(repeater('') ==  "")