"""
## Problem ##

Design a function that takes a string of words and returns
a dictionary. Each key represents a word length, and each
corresponding value represents the number of words of that length
in the string

Input: a string
Output: a dictionary

Explicit rules
- Words consist of any sequence of non-space chars (punctuation?)
- Words are separated by spaces
- Input might contain no words

Implicit rules
- Punctuation is included in word length (this is the meaning of
words consist of any seq of non-space chars)
- Capitalization/case makes no difference

Questions:
- How should we handle non-letter characters?
- Do any words have more than one space between them?
- What do we do with punctuation?
- Can the input contain only whitespace?
- Can the input begin with whitespace?

## Examples ##

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

## Data structure ##

A dictionary

Algorithm:

1. Set 'final results' to an empty dictionary
2. Cycle through the 'input' str and put each word as 
a separate item in 'words' list
3. Cycle through 'words'
- Calculate the length of each element
- If the element is a new length, add the length to 'final results'
and set the corresponding value to 1
- If the element is already in 'final results', add one to the
corresponding value
4. Return 'final results' once you've reached the end of 'words'

Implementation notes:

1. Use split method to split string into a list of words
2. Use len() function on each element to find len
3. Use dict.get(key, 0) + 1 to avoid KeyErrors when adding
elements to dict/incrementing

"""
def word_sizes(string):
    results = {}
    word_list = string.split()

    for word in word_list:
        results[len(word)] = results.get(len(word), 0) + 1
    
    return results

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

# Without dict.get method

# def word_sizes(string):
#     results = {}
#     word_list = string.split()

#     for word in word_list:
#         if len(word) not in results:
#             results[len(word)] = 1
#         else:
#             results[len(word)] += 1
    
#     return results

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})