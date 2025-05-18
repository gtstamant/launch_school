"""
## Problem ##
Input: a letter
Output: A diamond with the letter in the
center row

## Examples & Test Cases ##

1: A

A

2: C

  A
 B B
C   C
 B B
  A

Note: E is the fifth letter

1234A1234
123B1B123
12C123C
1D12345D
E1234567E


Test Case Info:
- Diamond class
-- No instantiation
-- make_diamond method, class or static

## Algorithm ##
Each string has a length of (letter_num - 1) * 2 + 1
There are (letter_num - 1) * 2 + 1 rows

Build each string one by one
total_padding = (letter_num - 1) * 2
left pad = (letter_num - 1)
right pad = (letter_num - 1)
center pad = left pad - right pad

strings = []
for letters up to letter
  if center pad = 0
    append 'A' to strings
  otherwise append left pad + letter + center pad + letter + right pad
  left pad - 1
  right pad - 1
  center pad + (2n - 1)

copy all but the last member of strings
reverse it and append it to strings


"""
class Diamond:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    @classmethod
    def _get_diamond(cls, center):
        diamond = []
        end = cls.alphabet.index(center)
        
        side_pad = end
        center_pad = 0
        for letter in cls.alphabet[:end + 1]:
            if center_pad:
                diamond.append(
                    f'{side_pad * ' '}{letter}'
                    f'{center_pad * ' '}'
                    f'{letter}{side_pad * ' '}'
                )
            else:
                diamond.append(
                    f'{side_pad * ' '}{letter}'
                    f'{side_pad * ' '}'
                )
            side_pad -= 1
            center_pad = (2 * end) - 2 * side_pad - 1
        
        return diamond + diamond[:-1][::-1]
    
    @classmethod
    def make_diamond(cls, center):
        return '\n'.join(cls._get_diamond(center)) + '\n'

print(Diamond.make_diamond('C'))