"""
## Problem:

Write a function that takes an integer input
and returns its maximum rotation as an output

Input: a number
Output: the maximum rotation of the `input` number

Explicit rules:
- Start with `input` and rotate one digit to the left
- Perform the same operation, leaving the first digit of
`input` in place and beginning with the second digit, if present
- Continue onward holding incremently larger groups of the 
right-most number in place

Implicit rules:
- Single number remains unchanged

Questions:
- What to do with empty inputs?
- Non-int inputs?
- Single number inputs?

## Examples:

print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845

## Data structure:
- No obvious need but let's see

## Algorithm:
- Save `len input` as variable
- Perform transformation on `input`
    - Begin with whole input string
    - Perform on successively smaller portions of string
- Return string

Transformation subprocess:
- Convert `input` to string
- Split `input` into two parts
    - First part is not to be transformed
    - Second part is to be transformed
- Slice the initial digit of `second part` and add to end
of `second part`
- Concatenate `first part` with modified `second part`

"""
def rotate_rightmost_digits(integer, count):
    num = str(integer)
    constant, to_rotate = num[:-count], num[-count:]
    to_rotate = to_rotate[1:] + to_rotate[0]
    
    return int(constant + to_rotate)

def max_rotation(integer):
    result = str(integer)
    for idx in range(len(result), 1, -1):
        result = rotate_rightmost_digits(result, idx)
    
    return result

print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845