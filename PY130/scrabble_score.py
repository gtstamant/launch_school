""""
Problem: Write a program that computes a scrabble score based on a word (string)

A scrabble score sums the value of all the tiles used for each word:

AEIOULNRST = 1
DG         = 2
BCMP       = 3
FHVWY      = 4
K          = 5
JX         = 8
QZ         = 10

Specifications:
- Receive a string that represents a word
- Sum up the value of all the letters
- Return an integer

Example:

'CABBAGE'

3 + 1 + 3 + 3 + 1 + 2 + 1 = 14


- Test Cases

- Scrabble class
- score method
- empty space of any kind is equivalent to 0

####

Data Structure:
- Dictionary that maps letters to their value
-- long key containing all relevant letters for a value

Algorithm:
- initialize total value to 0
- for each character in the input string (normalized to lower case)
-- look up the key that the character appears in
-- If the key has an associated value
--- add the value to the total value

return the total value

"""
class Scrabble:
    SCORES = {
        'aeioulnrst': 1,
        'dg': 2,
        'bcmp': 3,
        'fhvwy': 4,
        'k': 5,
        'jx': 8,
        'qz': 10
    }
    
    def __init__(self, word):
        self.word = word.casefold() if word else ''
    
    def _find_key(self, char):
        for key in Scrabble.SCORES.keys():
            if char in key:
                return key
    
    def score(self):
        total_score = 0
        for char in self.word:
            total_score += Scrabble.SCORES.get(self._find_key(char), 0)
        
        return total_score

    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()