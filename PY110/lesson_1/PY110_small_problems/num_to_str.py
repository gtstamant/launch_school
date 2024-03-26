"""
## Problem

Conver a string representation of an integer into an integer

Input: a string
Output: an int

Explicit requirements:
- Do not use conversion functions

Implicit requirements:
- All inputs are valid integers
- Can have 0
- No negative numbers

Questions:

- Negative or positive?
- Chance of invalid input?
- Change of non-int?

## Examples:

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

## Data structure

- Dictionary for conversion table

## Algorithm

1. Build a 'conversion' dictionary
2. Set 'result' to empty string
3. Convert each digit to string (subprocess)
4. Return 'result'

** Subprocess **

1. Extract first digit from input integer
- Get 'current power of 10' by subtracting one from current
length of string
- Integer divide digit by 10 ** 'current power'
2. Convert digit to string
3. Concatenate converted digit with 'result'
4. Remove the first digit (subprocess?)

Example case:

4321

To get 4 from 4321, we can do 4321 // 1000 (or 10 ** 3)
To get 3 from 321, we can do 321 // 100 (or 10 ** 2)
To get 2 from 21, we can do 21 // 10
To get 1 from 1, we can do 1 / 1

Implementation details:
- How to find base of number?
    - Could check if num is 0 and if not then divide by
    increasing 10 until it returns 0 and take
    previous as top power?

"""

def find_power(integer):

    counter = 0
    while True:
        integer = integer // 10
        if integer == 0:
            break
        counter += 1
    
    return counter

def integer_to_string(integer):
    conversion = {
        x:str(x) for x in range(10)
    }
    power = find_power(integer)
    result = ''

    while power >= 0:
        current_num = integer // (10 ** power)
        result += conversion[current_num]
        integer -= current_num * (10 ** power)
        power -= 1
    return result


# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

lst1 = [1]
lst2 = [2]

lst1.concat(lst2)
