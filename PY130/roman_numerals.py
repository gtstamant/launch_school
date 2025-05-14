"""
Problem: Write a program to convert decimal numbers into Roman numerals

Specifications:
- Takes an integer input
- Returns a string roman numeral
- Doesn't need to deal with numbers larger than 3000

Questions:
- RomanNumeral class
- Can it take floats?

Class Structure:
- RomanNumeral class
-- Takes an integer argument
-- to_roman method, no arguments

Roman Numerals:
1 = I
5 = V
10 = X
L = 50
C = 100
D = 500
M = 1000

Break points:

x4
x5
x9

I II III IV
V VI VII VIII
IX X 

XI XII XIII XIV

Data Structure:
- Strings
- Perhaps a dictionary to map values

Algorithm:
Get ones digit
- assign correct roman numeral
Get tens digit:
- assign correct roman numeral
Get hundreds digit:
- assign correct roman numeral
Get thousands digit:
- assign correct roman numeral


"""

class RomanNumeral:
    CONVERSIONS ={
        1000: 'M',
        900 : 'CM',
        500 : 'D',
        400 : 'CD',
        100 : 'C',
        90  : 'XC',
        50  : 'L',
        40  : 'XL',
        10  : 'X',
        9   : 'IX',
        5   : 'V',
        4   : 'IV',
        1   : 'I',
    }
    
    def __init__(self, number):
        self.number = number
    
    def to_roman(self):
        roman_numeral = ''
        number = self.number
        
        for key, value in RomanNumeral.CONVERSIONS.items():
            numeral, number = divmod(number, key)
            if numeral:
                roman_numeral += (value * numeral)
        
        return roman_numeral



num = RomanNumeral(1120)
print(num.to_roman())