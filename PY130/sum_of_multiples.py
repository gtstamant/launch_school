"""
## Problem ##
Inputs: a number (A) and a set of one or more other numbers (B)
- B has a default value of {3, 5}
Outputs: Sum of all the multiples of the numbers in B that are less than A

## Examples & Test Cases ##

1. 20, {3, 5}

sum(3, 5, 6, 9, 10, 12, 15, 18) = 78

- SumOfMultiples class
Instance Methods
-- init method, takes a set of numbers as argument, default to 3, 5

Class methods
- sum_up_to method
-- sums all multiples of 3 and 5 up to a number 


"""
class SumOfMultiples:
    BASES = {3, 5}

    def __init__(self, *bases):
        self.bases = bases if bases else SumOfMultiples.BASES

    def to(self, value):
        minimum = min(self.bases)
        return sum(num for num in range(minimum, value)
                               if any(num % base == 0 for base in self.bases))

    @classmethod
    def sum_up_to(cls, value):
        return SumOfMultiples().to(value)
