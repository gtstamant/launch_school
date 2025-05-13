"""
Problem:
Write a program that calculates the hamming distance between DNA strangs
- Hamming distance is the number of differences between DNA strands

Structure:
- DNA strands are a class
- DNA class constructor accepts a string that represents DNA strand
- Hamming distance method
-- Takes another DNA strand string as argument, compares against obj's string

Specifications:
- If two strands are different lengths, compare up to the end of shorter strand

Questions:
- Should we deal with invalid inputs?

Algorithm:

** DNA Comparison **
Let hamming distance = 0
Make a copy of each string
While both strings still have elements
- remove the first element from each list
- if the elements are different
-- add one to hamming distance

return the hamming distance

"""
class DNA:
    def __init__(self, strand):
        self._strand = strand
    
    def hamming_distance(self, other):
        differences = 0

        for self_char, other_char in zip(self._strand, other):
            if self_char != other_char:
                differences += 1

        return differences

        # if not isinstance(other, str):
        #     raise ValueError('DNA strands must be strings.')

        # self_copy = self._strand[:]

        # hamming_distance = 0
        # while self_copy and other:
        #     if self_copy[0] != other[0]:
        #         hamming_distance += 1
            
        #     self_copy, other = self_copy[1:], other[1:]
        
        # return hamming_distance