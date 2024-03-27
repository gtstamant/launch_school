# """"
# ## Program:

# Function should take a floating point number that represents
# an angle between 0 and 360 degrees. It returns a string 
# representation of the same angle in degrees, minutes, and seconds.

# Input: a float representation of a degree
# Output: a string representation of a degree

# Explicit requirements:
# - There are 360 degrees
# - Each degree is divided into 60 minutes (1 minute = 1/60 degree)
# - Each minute is divided into 60 seconds (1 second = 1/60 second)
# - Use a degree symbol (˚) to denote degrees
# - Use a single quote (') to denote minutes
# - Use a double quote (") to denote seconds

# Implicit requirements:
# - Seconds should finish with a back slash and two "" marks

# Questions:
# - Possibility of negative degrees?
# - What happens at 360/0?

# ## Examples:

# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# ## Data structure

# Perhaps an intermediate list?

# ## Algorithim

# Mental model:

# - We want to divide the degree by 1 to get the whole number part
# of the integer; this is the degree
# - We then need to convert the decimal remainder to minutes,
# - We need to divide the minutes by 1 to get the whole number part;
# these are the minutes
# - We then need to convert the decimal remainder to seconds

# Steps"

# 1. Set 'result' to an empty string
# 2. Set 'remainder' = 0
# 3. Convert 'current' (input) integer to degrees
#     - Divide 'input' by 1 and set to
#         - Whole number and decimal remainder (remember floating point issues)
#     - Add whole number to result, with degree symbol
#     - Set decimal to 'current'
# 4. Convert the decimal remainder to minutes
#     - Multiply 'current' by 60 (conversion factor, cur = x/60)
#     - Divide 'current' by 1 and set to
#         - Whole number and decimal remainder
#     - Add whole number to result, with minute symbol
#     - Set decimal to 'current
# 5. Convert the decimal remainder to seconds
#     - Multiply 'current' by 60
#     - Divide 'current' by 1
#     - Add whole number to result, with second symbol and backslash
# 6. Return result

# Implementation notes:
# - divmod(), but can I do without too?

# result = 76°

# current = 76.73
# - 76, .73

# current = .73 * 60
# current = 43.48
# - w, d = 43, .48
# current = 76° + 43'
# current = .48

# """

def get_minutes_and_seconds(remainder):
    conversions = []
    for _ in range(2):
        remainder *= 60
        whole, remainder = divmod(remainder, 1)
        conversions.append(whole)
    
    conversions = [
        (f'0{num:.0f}') if num < 10 else f'{num:.0f}'
        for num in conversions
    ]

    return conversions

def get_degree(degree):
    while degree < 0 or degree > 360:
        counter = 1
        if degree < 0:
            degree += 360 * counter
        elif degree > 360:
            degree -= 360 * counter
        counter += 1
    
    return degree

def dms(dec_degree):
    degree, remainder = divmod(dec_degree, 1)
    degree = get_degree(degree)
    minutes, seconds = get_minutes_and_seconds(remainder)

    return (f"{degree:.0f}°"
            f"{minutes}'"
            f'{seconds}"')

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"

"""
## Problem:

Rewrite the previous code to work with degree values less than 0
and greater than 360

Algorithim:

1. If positive
    - Subtract (360n) with incrementing n from number until number <= 360
2. If negative
    - Add (360n) with incr. n from number until number >= 0

"""