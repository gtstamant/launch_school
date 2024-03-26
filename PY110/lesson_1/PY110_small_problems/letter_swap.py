"""
## P: Understanding the problem

Given a string of words separated by spaces, 
write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, 
and that the string will always contain at least one word. 
You may also assume that each string contains nothing 
but words and spaces, and that there are no leading, trailing, 
or repeated spaces.

Input: a string of words
Output: a new string of words

Explicit requirements:
- String of words
- String will contain at least one word (no empty string)
- Each word is at least one character
- String will only contain words and spaces
- No leading, trailing, or repeated spaces

Implicit requirements:
- A word is defined as a seq of chars separated by spaces
- One letter string returns identical string
- Capitalization matters, letters should stay in same case
despite moving

## Examples:

'Oh what a wonderful day it is'
"hO thaw a londerfuw yad ti si"

'Abcde'
"ebcdA"

a 
a

## Data structure ##

No obvious need, though perhaps some intermediate
structure will be needed?

## Algorithim ##

1. Consider each word 
2. Swap the first and last letter (subprocess?)
3. Store the modified word in some sort of data structure
4. Return the modfied words in the form of a string

** Letter swap subprocess **

Could accomplish by slicing, but prone to off-by-one error.
How to deal with string len 1?

Implementation notes:

1. Use str.split to isolate words by returing list of all words?
2. Use list comprehension with suprocess transformation to 
build modified word list from original word list?
3. Return ' '.join(modified list)?

"""
def first_last(s):
    if len(s) == 1:
        return s
    return s[-1] + s[1:-1] + s[0]

# f string implementation

# def first_last(word):
#     if len(word) == 1:
#         return word
#     return f'{word[-1]}{word[1:-1]}{word[0]}'

def swap(s):
    swapped_words = [first_last(word) for word in s.split()]
    return ' '.join(swapped_words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True