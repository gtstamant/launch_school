"""
## Problem:

Write two functions: 
    - one that takes a rational number argument and returns a
    list of the denominators that are part of an egyptian
    franction representation of the number
    - one that takes a list of numbers in the same format and
    calculates the resulting rational number

## Problem 1

Input: a rational number
Output: a list of numbers

Explicit requirements:
- Requires the use of the fraction class module
- Egyptian fractions are composed of a sum of distinct unit fractions
    - i.e., no two fractions in the sum may be the same

Implicit requirements:
- The examples use the lowest possible denominators, try to match this

Questions:
- Is there more than one Egyptian fraction representation of a single rational number?
- Should we prioritize the return of some specific sequence of egyptian fractions?

## Examples
- See problem spec

## Data structure
- List; perhaps another list to keep track of failed attempts?

## Algorithm:

Mental model:

2     ==> 1/1  ==> 2 - 1
1     ==> 1/2  ==> 1 - 1/2
1/2   ==> 1/3  ==> 1/2 - 1/3 
1/6   ==> 0    (note here that 1/4, 1/5 are bigger than 1/6)

3     ==> 1/1  ==> 3 - 1
2     ==> 1/2  ==> 2 - 1/2 
3/2   ==> 1/3  ==> 3/2 - 1/3
7/6   ==> 1/4  ==> 


Algorithm:

# Setup
- Set the argument to the variable `num`
- Initialize the variable `result` to an empty list
- Initialize the variable `current denom` to 1

# Implementation
- Set `current fraction` to 1/`current denom`
- While num is not equal to 0
    - Check whether `num` - `current fraction` is >= 0
    - If yes:
        - Add `current denom` to `result`
        - Subtract `current fraction` from `num`
        - Increment `current denom` by 1
        - If `num` equals 0
            - Return `results`
    - If no:
        - Increment `current denom` by 1

Implementation notes:
- Import the fraction module

## Problem 2:

Write a function that takes a list of unit fraction denominators as an argument
and returns the rational number that results from summing them up

Input: a list of unique numbers
Output: a rational number in faction form

## Examples:
- 

"""

from fractions import Fraction

def egyptian(fraction):
    result        = []
    current_denom = 1

    while True:
        next_guess = fraction - Fraction(1, current_denom)
        if next_guess >= 0:
            result.append(current_denom)
            fraction = next_guess
            if next_guess == 0:
                return result
        current_denom += 1
    
def unegyptian(lst):
    return sum([Fraction(1, num) for num in lst])

from fractions import Fraction

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))