"""
## Problem:

Write a function that takes a positive integer argument
and returns that number with its digits reversed

Input: a positive integer
Output: a positive integer

***** Made an error here *****

Wrote an algorithim that output a string

******************************

Explicit requirements:

Implicit requirements:
- Leading zeros are dropped (i.e., 12000 > 21)

Questions:
- How should we deal with zeros?
- Non-int arguments?

## Data structure:

Maybe to keep track of intermediate results?

## Algorithm:


1. Initialize `reverse_num` as an empty string
2. Divide the `current` number input by 10 and store both the whole part and remainder
    - Add the remainder as a string to `reverse num`
    - Set the `current` to the whole part
    - Continue until whole part == 0
3. Return `reverse_num` with leading zeros stripped

Implementation notes:
- use str.lstrip('0') to strip out zeros
- use divmod(current, 10) to get whole num/remainder


"""

# def reverse_number(number):
#     result = ''

#     while number > 0:
#         # result += str(number % 10)
#         # number = number // 10
#         number, digit = divmod(number, 10)
#         result += str(digit)

#     return result.lstrip('0')

def reverse_number(number):
    return int(str(number)[::-1])

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1