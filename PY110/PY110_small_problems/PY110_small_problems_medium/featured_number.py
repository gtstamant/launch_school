"""
## Problem:

Write a function that takes an integer argument and
returns the next featured number greater than the integer

Input: an integer
Output: an integer that is a featured number

Explicit requirements:
- A featured number must be:
    - odd
    - multiple of 7
    - no repeated digits
- The largest possible featured number is 9876543201

Implicit requirements:
- If the number is too large:
    - Return 'There is no possible number that fulfills the requirement.s'

Questions:
- Can we assume a valid integer input?
- How should we respond to an empty input?
- Are inputs larger than the largest featured number allowed?

## Examples:
- See question spec

## Data structure:
- Perhaps a list for intermediate data?

## Algorithm:
- Take `input` variable
- Find closest multiple of seven > `input` (subprocess)
- Set closest multiple of seven to `current`
    - If current meets conditions (subprocess)
        - return current
    - If not
        - Increment current by 7 and return to condition test

** Suprocess: find closest multiple of seven > `current` **
- If current is a multiple of 7
    - return current value
- If not
    - Increment current by one and return to beginning of process

** Subprocess: check if current meets conditions **
# Note that only considering multiples of 7

- Check if `current` is divisible by two
- Check if `current` contains repeated digits (subprocess)

** Subprocess: check for repeated digits **
- Convert `current` to a string
- Convert `current string` into a list of individual digits
- Initialize `no duplicates` as an empty list
- Cycle through each element of `current list`
    - If the element is not in `no duplicates`
        - Add the element to `no duplicates`
    - If an element is not added
        - return False
- Return true

Implementation notes:
- Don't forget the largest possible number!

"""

MAX_FEATURED = 9876543201

def is_odd(num):
    return num % 2 != 0

def get_next_mult_7(num):
    num += 1
    while num % 7 != 0 or num % 2 == 0:
            num += 1

    return num

def no_repeated_dig(num):
    num_lst = list(str(num))
    return len(num_lst) == len(set(num_lst))

# def is_featured_num(mult_of_7):
#     return is_odd(mult_of_7) and no_repeated_dig(mult_of_7)

def featured(num):
    if num >= MAX_FEATURED:
        return ('There is no possible number' 
                'that fulfills those requirements.')
    
    current_guess = get_next_mult_7(num)
    while not no_repeated_dig(current_guess):
        current_guess += 14
    
    return current_guess

print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."