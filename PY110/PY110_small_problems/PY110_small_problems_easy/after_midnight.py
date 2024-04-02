"""
## Problem

Write a function that takes a time expressed
in minutes before or after midnight and returns
the same time in 24-hour format

Input: an integer
Output: a string representing a 24-hour format time

Explicit requirements:
- Any integer should work
- Should accept positive numbers (after midnight) and
negative numbers (before midnight)
- Cannot use datetime module

Implicit requirements:
- 

Questions:
- What happens when a number goes over 12 hours in length?
- Do we need to worry about seconds?

## Examples:

print(time_of_day(0) == "00:00")
print(time_of_day(-3) == "23:57")       
print(time_of_day(35) == "00:35")       
print(time_of_day(-1437) == "00:03")    
print(time_of_day(3000) == "02:00")    
print(time_of_day(800) == "13:20")     
print(time_of_day(-4231) == "01:29")    


24    <==   12 <== 0 ==> 12  ==> 24
-1440 <== -720 <== 0 ==> 720 ==> 1440

-1437

## Data structure:

Nothing particular needed

## Algorithim:
1. Reduce absolute value of input by 1440 until it is
between 0 and 1440 inclusive
2. Divide input by 60
- If positive
    - Whole part of quotient is the hours
    - Remainder * 60 are the minutes
- If negative
    - Subtract quotient from 24 (actually add)
    - Whole part of result is hour
    - Remainder * 60 are the minutes

Implementation notes:
- Use while (abs(input) - 1440n) > 1440 
    - dont forget to increment n!

"""

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

def get_time(time):
    time = time % MINUTES_IN_DAY
    
    if time < 0:
        time += MINUTES_IN_DAY

    hours, min = divmod(time, MINUTES_IN_HOUR)

    return (hours, min)

def time_of_day(time):
    hours, min = get_time(time)

    return f'{int(hours):02d}:{int(min):02d}'


# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

import datetime as dt

delta = dt.timedelta(minutes=-3)

print(delta)




