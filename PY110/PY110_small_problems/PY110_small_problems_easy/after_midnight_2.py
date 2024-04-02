"""
## Problem

Write two functions:
- One returns the number of minutes before midnight
- One returns the number of minutes after midnight

Input: a string representation of a time in 24-hour form
Output: an integer

Explicit requirements:
- Both functions should return a value between 0 and 1439
- No datetime module

Implicit requirements:
- 

## Examples:

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

## Data structure:
- Nothing specific needed?

## Algorithm:

Mental model:

The output is a total in minutes. We can get the output number
for the time after midnight by:

1. Determining the total number of minutes in the hour portion
of the 'input' time 
2. Adding that to the minute portion of the 'input' time.

- We need to be careful around the 0 point.

For the time before midnight, we just need to get the time
after midnight and subtract it from the number of minutes in
a day

Algorithm:

Time after midnight:

1. Split the input string at the ':'
2. Convert both parts to integers
3. Multiply hours times number of minutes in an hour
4. Add min per hour to the minutes portion
5. Return the value
-- add conditional to return 0 if total min % mins in day is zero

Time before midnight:
1. Call time before midnight
2. Return minutes in day - result

Implementaiton notes:

- Split string with index search for ':'

"""

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

def after_midnight(str_time):
    hours, minutes = [int(unit) for unit in str_time.split(':')]
    return ((hours * MINUTES_IN_HOUR) + minutes) % MINUTES_IN_DAY

def before_midnight(str_time):
    total_mins = MINUTES_IN_DAY - after_midnight(str_time)
    if total_mins == MINUTES_IN_DAY:
        return 0
    
    return total_mins

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True