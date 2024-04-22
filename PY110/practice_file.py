"""
add method set

chained action (element reference, element reassignment)

lst3 = [['abc'], ['def'], {'third': ['ghi']}] 
==> access 'g'

https://launchschool.com/lessons/76ecb255/assignments/c28a3c63
Practice Problem 3 

Sets:

Union method vs. update method

"""

"""
1. B, C
2. A, B, C, D
3. B, D
4. A, C, D
5. A, B, D


"""

"""
Problem:
Write a function that takes a float representation of an angle
between 0 and 360 degrees and returns a string representation of
that angle in degrees, minutes, and seconds

Input: a float
Output: a string

Questions:
- What is a minute in this context?
- What is a second in this context?
- Can we assume a valid float input?
- Should we worry about degrees over 360 or less than 0?

Explicit requirements:
- Convert float representation of an angle into a string
- Use degrees, minutes ( 1/60th of a degree) and seconds (1/60th of a minute)
- Use ˚ for degrees, ' for minutes, and " for seconds

Implicit requirements:
- You may assume a valid float input
- Inputs are between 0 and 360 inclusive
- Minutes and seconds should be in the form 00

Examples: 
- See spec

Data structure:
- None obviously needed

Algorithm:
- Set `result` to an empty list
- while the length of result is less than 3
    - Divide `input` by 1
        - Convert the dividend into a string and add to `result`
        - Set `input` equal to the remainder * 60

- return a formatted string from result
    - take the first element, add˚
    - take the second element, add ', make sure to display as 00
    - take the third element, add ", make sure to display as 00

"""

def dms(angle):
    result = []
    
    while len(result) < 3:
        dividend, remainder = divmod(angle, 1)
        result.append(int(dividend))
        angle = remainder * 60
    
    return f'''{result[0]}˚{result[1]:02d}'{result[2]:02d}"'''

print(dms(30)) # == "30°00'00\"")
print(dms(76.73)) # == "76°43'48\"")
print(dms(254.6)) # == "254°35'59\"")
print(dms(93.034773)) # == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")