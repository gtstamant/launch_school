"""
Problem:
Modify a preexisting string-to-integer function
to take account of sign

Input: a string representation of an integer
Output: an integer

Explicit requirements:
- Int should be positive if first char in str a '+'
- Int should be positive if first char in str a digit
- Int should be negative if first char in str '-'
- String will contain a valid number
- No conversion functions

Other implicit and explicit requirements remain the same

Examples:

"4321" ==> 4321
"-570" ==> -570
"+100"  ==> 100

Data Structure:

Dict for conversion table

Algorithim:

1. Check first char in str
- if it isn't a negative sign, return result of str to int function
- if it is a negative sign, return the negative result of str to int function

"""

# def string_to_signed_integer(str_int):
#     if str_int[0] == '-':
#         return -string_to_integer(str_int[1:])
#     if str_int[0] == '+':
#         return string_to_integer(str_int[1:])
#     return string_to_integer(str_int)

# Refactored with match/case

def string_to_signed_integer(str_int):
    match str_int[0]:
        case '-': return -string_to_integer(str_int[1:])
        case '+': return  string_to_integer(str_int[1:])
        case  _ : return  string_to_integer(str_int)

def string_to_integer(str_int):
    conversion = {
        str(num): num for num in range(10)
    }

    total = 0
    for num in str_int:
        total = (total * 10) + conversion[num]
    
    return total

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True