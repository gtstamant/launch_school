"""
## Problem

Input: a string of digits
Output: an integer

Explicit requirements:
- Given a string of digits
- Cannot use built-in conversion functions
- No non-numeric characters
- No + or - symbols

Impliciit requirements:
- String of digits must be a representation of an integer

Questions:
- What does it mean for the function to 'calculate' results?

## Examples 

"4321" ==> 4321
"570" ==> 570

Data structure:

- May need a dictionary that correlates string representations
of integers with the integers themselves
- Is another structure needed to store the digit place,
i.e. 10s, 100s, etc?

Algorithim:

1. Set variable 'total' equal to 0
2. Consider the string digit by digit (subprocess?)
- Access the corresponding integer by looking up the string digit
in the conversion table
- Multiply the appropriate integer by the right power of 10
- Add the product to 'total
3. Return total

Implementation notes:

- To get 10 ** n, 

"4321"

4 * 10 ** 3 (3 = len - 1)
3 * 10 ** 2 (2 = len - 2)
2 * 10 ** 1 (1 = len - 3)
1 * 10 ** 0 (0 = len - 4)

So range(1, len + 1) [1, 2, 3, 4]

"""

# def string_to_integer(str_int):
#     conversion = {
#         str(num): num for num in range(10)
#     }
#     total = 0
#     for idx, char in enumerate(str_int):
#         power = 10 ** (len(str_int) - (idx + 1))
#         total += conversion[char] * power

#     return total

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

#better implementation

def string_to_integer(str_int):
    conversion = {
        str(num): num for num in range(10)
    }

    total = 0
    for num in str_int:
        total = (total * 10) + conversion[num]
    
    return total

# 4 ==> 40 + 3 ==> 430 + 2 ==> 432 + 1

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

def hexadecimal_to_integer(str_hex):
    conversion = {
        str(x): x for x in range(10)
    }

    conversion_2 = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    conversion |= conversion_2
    
    total = 0
    for num in str_hex:
        total = (total * 16) + conversion[num.upper()]
    
    return total

print(hexadecimal_to_integer('4D9f') == 19871)  # True