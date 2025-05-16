"""
## Problem ##

Create a program that converts from an octal system to a decimal number output

Base-8 system, from rightmost digit:
digit * 8^0
digit * 8^1
digit * 8^n

sum all digits

233 #octal

2 * 8^2 + 3 * 8^1 + 3 * 8^0

= (2 * 64) + (3 * 8) + (3)
= 128 + 24 + 3
= 155

Rules:
  Explicit rules
    - Accept an octal string
    - Treat as invalid octal 0 (?)
    - Valid digits are 0,1,2,3,4,5,6,7

In brief:

Go digit-by-digit of the octal input string, computing the appropriate value
and returning the sum of the values as an integer (I think, but check return)

## Examples & Test Cases #

Octal class
- takes a string argument
- to_decimal method, returns a base-10 integer
-- invalid octal returns decimal 0, non digits
-- Octal 8 is invalid, returns 0 (would be represented as 10)
-- Octal 9 also invalid
-- Octal 6789 invaild (both 8, 9 invalid)
-- Occtal 011 is equal to Octal 11, returns 9 -- leading 0s not counted/an issue

## Algorithm ##

input - 11
power = 0
total = 0

Starting from the right of the input
- iterate through each character
-- convert the character to an integer
-- multiply the character times 8^power
-- increase power by 1

(naturally takes care of leading 0s)

** validate octal **
iterate through each character in octal
-- if character not in 01234567 (strings)
--- return 0

"""
class Octal:
    VALID_DIGITS = '01234567'
    def __init__(self, octal):
        self.octal = octal
    
    # @classmethod
    # def _invalid_octal(cls, octal):
    #     for char in octal:
    #         if char not in cls.VALID_DIGITS:
    #             return True
        
    #     return False

    # def to_decimal(self):
    #     if Octal._invalid_octal(self.octal):
    #         return 0

    #     return sum(int(char) * 8**idx for idx, char in enumerate(self.octal[::-1]))

    @classmethod
    def _invalid_digit(cls, digit):
        return digit not in cls.VALID_DIGITS
    
    def to_decimal(self):
        total = 0

        for idx, char in enumerate(self.octal[::-1]):
            if Octal._invalid_digit(char):
                return 0
                
            total += int(char) * 8**idx
        
        return total