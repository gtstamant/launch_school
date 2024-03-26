"""
## Problem

Take an integer and conver it into a number represented 
in string format

Input: an integer
Output: a string

Explicit requirements:
- Do not use built-in conversion methods
- Input will be non-negative
- You should produce the output by manipulating the number

Implicit requirements:
- Input can be 0

Questions:
- Can the input be a non-number?
- Can the input be 0?

## Examples

ExamplesCopy Code
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

## Data structure

None needed?

## Algorithm

Mental model:

Extract the individual digits from right to left,
adding them to the beginning of an empty string.

1. Set the divisor to 10
2. Set 'result' to an empty string
3. For each digit in 'input'
    - Divide 'input' by divisor
    - Obtain remainder and add to the beginning of the empty string
    - Set the non-remainder part of the dividend to 'input'
    - Multiply 'divisor' times 10
4. Return 'result'

Implementation notes:

1. Use the % operator to obtain remainders
2. Use the // operator to obtain non-remainder part of dividend
3. Use conditional statement to track when number drops to 0?

4321

4321 % 10 ==> 1
4321 //= 10 ==> 432

432 % 10 ==> 2
432 //= 10 ==> 43

43 % 10 ==> 3
43 //= 10 ==> 4

4 % 10 ==> 4
4 // 10 ==> 0

"""

# def integer_to_string(integer):
#     conversion = {
#         x:str(x) for x in range(10)
#     }
    
#     # if integer == 0:
#     #     return conversion[integer]

#     result = ''

#     while integer > 0:
#         current_digit = integer % 10
#         result = (conversion[current_digit] 
#                   + result)
#         integer //= 10
    
#     return result or '0'

# print(integer_to_string(4321))              # True
# print(integer_to_string(0))                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

# Divmod solution

# def check_sign(integer):
#     sign = ''
#     if integer < 0:
#         sign = '-'
#     elif integer > 0:
#         sign = '+'
#     return sign

# def signed_integer_to_string(integer):
#     conv = {
#         num: str(num) for num in range(10)
#     }
    
#     sign = check_sign(integer)
#     integer = abs(integer)
#     result = ''
    
#     while integer > 0:
#         integer, remainder = divmod(integer, 10)
#         result = conv[remainder] + result

#     return f'{sign}{result}' or '0'

# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123))   # True
# print(signed_integer_to_string(0) == "0")         # True

def integer_to_string(integer):
    conv = {
        x:str(x) for x in range(10)
    }

    result = ''
    while integer > 0:
        integer, digit = divmod(integer, 10)
        result = conv[digit] + result
    
    return result or '0'

# print(integer_to_string(4321) == '4321')              # True
# print(integer_to_string(0) == '0')                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

def signed_integer_to_string(integer):
    if not integer:
        return integer_to_string(integer)
    elif integer > 0:
        return f'+{integer_to_string(integer)}'
    return f'-{integer_to_string(-integer)}'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123)== '-123')   # True
print(signed_integer_to_string(0) == "0")         # True