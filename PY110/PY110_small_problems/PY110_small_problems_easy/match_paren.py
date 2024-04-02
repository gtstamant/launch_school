"""
## Problem:

Compose a function that takes a string and returns True
if all the parentheses in the string are properly balanced and
False if they are not.

Explicit requirements:
- Properly balanced parentheses occur in matching ( ) pairs

Implicit requirements:
- Nested parentheses can be properly balanced

Questions:
- Can nested parentheses be properly balanced?
- How should we handle an empty string?
- How should we handle a string with no parentheses?

## Examples:

print(is_balanced("What (is) this?") == True)
print(is_balanced("What is) this?") == False)
print(is_balanced("What (is this?") == False)
print(is_balanced("((What) (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ((is))) up(") == False)

## Data structure

None needed

## Algorithm:

Iterate through the characters of the string,
keeping track of each `(` char and whether it
is closed by a `)` char.
    - If a `(` char is not closed, return False
    - If a `)` char is not opened, return False
Return True

Implementation notes:
- Track whether num closed is ever higher than num opened
- check at end whether all opened have been closed

"""

# def is_balanced(string):
#     open_parens = 0

#     for char in string:
#         if char == '(':
#             open_parens += 1
#         elif char == ')':
#             open_parens -= 1
#         if open_parens < 0:
#             return False
#     return open_parens == 0

# print(is_balanced("What (is) this?") == True)
# print(is_balanced("What is) this?") == False)
# print(is_balanced("What (is this?") == False)
# print(is_balanced("((What) (is this))?") == True)
# print(is_balanced("((What)) (is this))?") == False)
# print(is_balanced("Hey!") == True)
# print(is_balanced(")Hey!(") == False)
# print(is_balanced("What ((is))) up(") == False)

def is_balanced(string):
    parens = {'{': '}', '(': ')', '[':']', '\"':'\"', "\'": "\'"}
    stack = []

    for char in string:
        if char in parens.keys():
            stack.append(char)
        if char in parens.values():
            if not stack or parens.get(stack.pop()) != char:
                return False
    
    return not stack

print(is_balanced("{}") == True)
print(is_balanced("[]") == True)
print(is_balanced("()") == True)
print(is_balanced("{[({})]}") == True)
print(is_balanced("\"{[('')]}\"") == True) 
print(is_balanced("Hello [Python] (asdf).") == True)
print(is_balanced("{[()stacks]} are {kool[()]}") == True)
print(is_balanced("{[}]") == False)
print(is_balanced("({[})") == False)
print(is_balanced("][") == False)