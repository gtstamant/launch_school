"""
## Problem:

Write a function that rotates a some number of digits of
a number. It should take two arguments: the number and the
number of digits that you want to rotate. To accomplish the
rotation, move the first of the digits to be rotated to the
end of the number and the remaining all one place to the left.

For example:

735291, 4 ==> 732915

Input: an integer, a number of digits to rotate
Output: rotated integer


Explicit rules:
- See problem instruction

Questions:
- How to handle non-number inputs?
- Return input when 0 digits are to be rotated?
- How to handle number of digits to be rotated
longer than length of number

## Examples:

print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917

## Data structure
- Easiest solution may involve turning the number
into a string

## Algorithm:
- Turn the `input` into a str called `str_num`
- Remove the character indexed at `count` subtracted from
the length of the string
- Save the removed `character` and append it to the end of
`str_num`
- Convert `str_num` to an integer and return it

"""

def rotate_rightmost_digits(number, count):
    lst_num = list(str(number))
    last_char = lst_num.pop(-count)
    lst_num.append(last_char)

    return int(''.join(lst_num))

print(rotate_rightmost_digits(735291, 2) == 735219)
print(rotate_rightmost_digits(735291, 3) == 735912)
print(rotate_rightmost_digits(735291, 1) == 735291)
print(rotate_rightmost_digits(735291, 4) == 732915)
print(rotate_rightmost_digits(735291, 5) == 752913)
print(rotate_rightmost_digits(735291, 6) == 352917)