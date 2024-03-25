"""
## Problem ##

Input: a string
Output: true if string a palindrome, false otherwise

Explicit rules:
- Case does not matter
- Ignore all non alphanumeric characters

Implicit rules:
- Expect a string as input
- No non-English chars
- No empty strings as input

## Examples ##

'madam'             True
'356653'            False
'356635'            False
'356a653'           True
'123ab321'          False
'Madam'             True
'Madam, I'm Adam'   True

Data structure:

Probably don't need one

Algorithm:

1. Set variable 'clean text' equal to empty string
2. Go through each character of 'input' string
- If the character is alphanumeric
    - Make lower case
    - Add to 'clean text'
3. Check whether 'clean text' is a palindrome

"""

def is_real_palindrome(s):
    clean_text = ''
    for char in s:
        if char.isalnum():
            clean_text += char.casefold()
    
    return clean_text == clean_text[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True