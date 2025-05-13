# /^(A|The) [a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z] (dog|cat)$/
# check that the anchors are necessary here; given the
# pattern, it would seem like they are not

#/\A.*\?\Z/
# Also why do we need the anchor at the beginning of
# a line that matches zero or more of every char

#\A(\d+)((,\d+){2}|(,\d+){5,})$

#<h1>.+?<\/h1>

# ask LS bot about the tendency to use ^ instead of \A

import re

def danish(string):
    return re.sub(r'\b(apple|blueberry|cherry)\b', 
                  'danish', 
                  string, 
                  count=1)

print(danish('An apple a day keeps the doctor away'))
# -> 'An danish a day keeps the doctor away'

print(danish('My favorite is blueberry pie'))
# -> 'My favorite is danish pie'

print(danish('The cherry of my eye'))
# -> 'The danish of my eye'

print(danish('apple. cherry. blueberry.'))
# -> 'danish. cherry. blueberry.'

print(danish('I love pineapple'))
# -> 'I love pineapple'