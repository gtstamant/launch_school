"""
## Problem:

Compose a function
- It should take a string argument
- Double every consonant in the string
- Return the result as a new string

Input: a string
Output: a string

Explicit requirements:
- Do not double vowels, digits, punctuation, or whitespace
- Only ASCII characters included in argument

Implicit requirements:
- Capitals remain the same

Questions:
- How should we treat an empty string?
- Do we need to worry about capitalization?

## Examples:

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

## Data structure:

May need a list or string to hold all consonants?

## Algorithim:

1. Initialize a new string, 'result', and assign to empty string
2. Cycle through each character in the 'input' string
    - Check if the character is a consonant
    - If so
        - Add it twice to 'result'
    - If not
        - Add it to result (only once)
3. Return 'result

Implementation notes:
- Remember to account for capitals in both vowels and consonants
- Can I use ascii chart to programatically generate the list of
consonants?

"""

VOWELS = 'aeiou'
CONSONANTS = {
    chr(unicode_pos) for unicode_pos in range(ord('a'), ord('z') + 1)
    if chr(unicode_pos) not in VOWELS
}

def is_consonant(char):
    return char not in VOWELS and char.isalpha()

def double_consonants(input_str):
    result_str = ''.join([char * 2 if is_consonant(char.lower()) else char
                          for char in input_str])
    return result_str


# def double_consonants(input_str):
#     result_str = ''.join([char * 2 if char.casefold() in CONSONANTS else char
#                          for char in input_str])

# def double_consonants(string):
#     result = ''

#     for char in string:
#         if is_consonant(char.lower()):
#             result += (char * 2)
#         else:
#             result += (char)

#     return result

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")