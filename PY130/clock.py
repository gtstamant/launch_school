"""
## Problem ##
Create a clock with no reference to date
- Add and subtract minutes from the time
- Don't mutate Clock object, return new
- Two equal time clock objects should be equal

## Examples & Test Cases ##
Clock class
- Doesn't seem to get initialized directly
- Clock.at method (class or static)
-- First argument taken as hours
-- Second argument taken as minutes
-- + operator adds minutes
-- - operator subtracts minutes

Note that time is displayed in 24hr system

## Algorithm ##

** time calculator **

***Calculate minutes***
Take minutes
modulo division by 60
-- the remainder is the final minutes
-- the quotient is extra hours

**Calculate hours**
Take current hours
-- add extra hours
-- modulo division by 24
-- hours is the modulus

** string representer **
Transform time into string

"""
class Clock:
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24

    def __init__(self, hours, minutes):
        extra_hours, self.minutes = divmod(minutes, 
                                      Clock.MINUTES_IN_HOUR)
        self.hours = (hours + extra_hours) % Clock.HOURS_IN_DAY

    @classmethod
    def at(cls, hours, minutes=0):
        return Clock(hours, minutes)

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'
    
    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        new_minutes = self.minutes + other
        return Clock.at(self.hours, new_minutes)
    
    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        new_minutes = self.minutes - other
        return Clock.at(self.hours, new_minutes)
    
    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        
        return str(self) == str(other)

    def __ne__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented

        return str(self) != str(other)       
