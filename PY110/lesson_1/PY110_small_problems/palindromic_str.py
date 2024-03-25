"""
## Problem ##

Input: a string
Output: True if input string a palindrome, false otherwise

Explicit rules:
- Case matters
- All characters matter (i.e., including whitespace)

Implicit rules:
- Input strings can have spaces and non-alphanumeric characters

Questions:
- Can strings contain non-English alphabets?
- What should an empty string return?
- Is a single letter considered a palindrome?

## Examples ##

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
print(is_palindrome('Madam') == False)
print(is_palindrome("madam i'm adam") == False)

Data Structure:

May need a temporary structure, like a list, to hold
data, but probably not.

Algorithm:

1. Check if string is a palindrome
2. Return result

## Recursive Algorithm ##

1. Check if string has a length of 1 or 0
- If so, return True
- If not, go on to next step
2. Check if the first and last character are equal
- If so, repeat from step 1 onwards
- If not, return false

## Non-recursive Algorithm
1. Check if input string has an even or odd length
- If odd, calculate middle index and split string into two strings
    - reverse second string and check if equal to first string
    - return True if equal, False otherwise
- If even, calculate middle and split string into two
    - reverse second string and check if equal to first string
    - return True if equal, false otherwise

"""

def is_palindrome(my_string):
    return my_string == my_string[::-1]

def is_palindrome_recursive(my_string):
    if len(my_string) == 0 or len(my_string) == 1:
        return True
    else:
        if my_string[0] == my_string[-1]:
            return is_palindrome_recursive(my_string[1:-1])
        return False

def is_pal_loop(my_string):
    midpoint = len(my_string) // 2

    if len(my_string) % 2 == 0:
        if my_string[:midpoint] == my_string[:midpoint - 1:-1]:
            return True
    else:
        if my_string[:midpoint] == my_string[:midpoint:-1]:
            return True
    return False

print(is_pal_loop('madam') == True)
print(is_pal_loop('356653') == True)
print(is_pal_loop('356635') == False)

# case matters
print(is_pal_loop('Madam') == False)

# all characters matter
print(is_pal_loop("madam i'm adam") == False)