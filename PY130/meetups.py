"""
## Problem ##
Class that represents a meetup date
Input: month (1-12), year (e.g. 2021), 
Descriptor: 'first' — 'fifth', 'last', 'teenth'
-- descriptor strings case insensitive
-- teenth means a day that ends in teenth
one for each day in the month
-- Days are case-insensitive strings

## Examples & Test Cases
Init:
- Meetup(2013, 12)
day method
- 'Tuesday', 'second'
= date(2013, 12, 10)

For 'fifth' if none, return None

## Data structure ##

Working with strings and datetime objects

## Algorithm ##

__init__

take year and month inputs
save to instance variables

** day **
Loop through each day of the month
- check if it matches the descriptor (helper)
- if it matches, return the date object
  using year, month, day

** descriptor checker **

*** first - fifth ***
Initialize candidates to an empty list
For each day in the month
-- add candidate day to candidates
-- if length of candidates is equal to descriptor
--- return the last member of candidates

*** last ***
For each day in the month
-- add candidate day to candidates
-- return last member of candidates

*** teenth ***
For each day in the month
-- add candidate day to candidate if the number is found
in teenth list (class variable)
-- return candidate day

"""
from datetime import date, timedelta

class Meetup:
    WEEKDAYS = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }

    DESCRIPTORS = {
        'first': 1,
        'second': 2,
        'third' : 3,
        'fourth': 4,
        'fifth' : 5,
        'last'  : 'last',
    }

    def __init__(self, year, month):
        self.year = year
        self.month = month
    
    def day(self, weekday, descriptor):
        day = self._get_day(weekday.capitalize(), descriptor.casefold())
        return date(self.year, self.month, day) if day else None
    
    def _get_day(self, weekday, descriptor):
        match descriptor:
            case 'teenth': return self._teenth_day(weekday)
            case _       : return self._number_day(weekday, descriptor)

    def _number_day(self, weekday, descriptor):
        candidates = []
        day = 1

        while True:
            current_date = date(self.year, self.month, day)
            if current_date.weekday() == Meetup.WEEKDAYS[weekday]:
                candidates.append(day)

                if len(candidates) == Meetup.DESCRIPTORS[descriptor]:
                    return day
            
            if current_date.month != (current_date + timedelta(days=1)).month:
                return candidates[-1] if descriptor == 'last' else None

            day += 1

    def _teenth_day(self, weekday):
        for day in range(13, 20):
            if date(self.year, self.month, day).weekday() == Meetup.WEEKDAYS[weekday]:
                return day
