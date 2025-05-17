"""
## Problem ##
Input: string of digits and integer
Output: all possible series of consecutive digits
of length integer
- output lists of ints

-note consecutive means in the order
of the input string

Rules:
- if the integer is longer than the series
raise an error (ValueError)

## Examples & Test Cases ##
'01234'
-- 012, 123, 234

Series class
- __init__ takes a string of digits
- slices method, takes an integer

## Data Stucture ##

Lists might be helpful

## Algorithm ##

set start = 0
set end = size of string
set substrings = []

Get the substring indexed between start and end
- add it to substrings
- increment start and end by one
-- if end equals length of string
--- return substrings


"""
class Series:
    def __init__(self, series):
        self.series = series
    
    def slices(self, size):
        if size > len(self.series):
            raise ValueError('Slice is too long!')

        substrings = [self.series[idx : idx + size] for idx in range(len(self.series) - size + 1)]
        return [[int(char) for char in substring] for substring in substrings]

    # def slices(self, size):
    #     if size > len(self.series):
    #         raise ValueError('Slice is too long!')
        
    #     substrings = []
    #     start = 0
    #     end = size
        
    #     while end <= len(self.series):
    #         substrings.append(self.series[start:end])      
    #         start += 1
    #         end += 1

    #     return [[int(char) for char in substring] for substring in substrings]

