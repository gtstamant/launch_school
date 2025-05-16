"""
## Problem ##
Input: Integer
Output: a string, 'perfect', 'abundant', 'deficient'

Perfect numbers
- Have an Aliquot sum equal to the original number

Abundant numbers
- Have an aliquot sum greater than the original number

Deficient numbers
- Have an aliquot sum less than the origin anumber

Aliquot sum
- the sum of the positive divisors of a number
- divisors include one but exclude the number itself

Rules
- Explicit requirements:
-- take a integer argument
-- return a string

- Implicit requirements:
-- Do we need to deal with invalid arguments?
-- Is this a class/method structure?
-- What about 0?

## Examples ##

Example 1: 6

1 + 2 + 3 = 6, 'perfect'

Program Structure:
- PerfectNumber class
-- no instantiation apparently, only used for a class or static method

- classify method
-- Class method or potentially static method

## Algorithm ##

- Determine all the positive divisiors of the input
- Sum the divisors together
- classify number

** get divisors **
- Largest divisor is always less than or equal to half of the input

- initialize aliquot sum to 0
- Iterate all integers between one and the largest possible divisor
-- if the integer divides evenly into the input number
--- add the integer to the aliquot sum

return the aliquot sum

** classify number **
- get the aliquot sum
-- if it equals the input number
--- return 'perfect'
-- if it is smaller than the input number
--- return 'deficiecient
- return 'abundant'

"""
class PerfectNumber:
    @staticmethod
    def _get_divisor_sum(input):
        return sum(num for num in range(1, input // 2 + 1) if input % num == 0)

    @classmethod
    def classify(cls, input):
        if input <= 0:
            raise ValueError('Input must be a positive integer')

        divisor_sum = cls._get_divisor_sum(input)

        if divisor_sum == input:
            return 'perfect'
        if divisor_sum < input:
            return 'deficient'
        
        return 'abundant'
