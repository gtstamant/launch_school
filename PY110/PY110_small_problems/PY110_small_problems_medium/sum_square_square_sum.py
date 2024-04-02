"""
## Problem:

Write a function that computes the difference between
the square of the sum of the first `count` (argument)
positive integers and the sum of the squares of the 
first `count` (argument) positive integers

Input: integer
Output: integer

Explicit requirements:
- Square of the sum of the first `count` pos ints:
    - (1 + 2 + ... + n) ** 2
- Sum of the squares of the first `count` pos ints:
    - 1**2 + 2**2 + 3**2

Implicit requirements:
- Argument always a positive int

Questions:
- Will argument always be a positive int?

## Examples:
- See problem spec

## Data structure:
- Perhaps a pair of lists for intermediate values?

## Algorithm:
- Compute the square of the sums of `count` pos ints (subprocess)
- Compute the sum of the squares of `count` pos ints (subprocess)
- Return the difference between the two

** Suprocess: square of sums **
- Generate a list of integers between 1 and count, inclusive
- Return their sum

** Suprocess: sum of squares
- Generate a list of the squares of the integers between 1 and count, inclusive
- Return their sum

Implementation notes:
- Sum of squares easily solved by list comprehension with range
- Don't forget that range stop value is exclusive

"""

def sum_square_difference(count):
    square_of_sum = sum(range(count + 1)) ** 2
    sum_of_squares = sum([num ** 2 for num in range(count + 1)])

    return square_of_sum - sum_of_squares

print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150