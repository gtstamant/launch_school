"""
## Problem ##
Generate a Robot object with a random name

Rules:
- Each Robot object receives a random name
- Robots get a new random name when rebooted
- Collisions not allowed

## Examples & Test Cases
Names of the form:
[A-Z]{2}\\d{3}

Robot class
- no arguments to __init__
- .name attribute
- reset method, changes .name attribute

"""
import string
from random import choice

class Robot:
    names = set()
    LETTERS = string.ascii_uppercase
    NUMBERS = string.digits

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            self._reset_name()
        
        return self._name

    def _reset_name(self):
        while True:
            self._name = Robot._new_name()
            if self._name not in Robot.names:
                break

        Robot._record_name(self._name)

    @classmethod
    def _record_name(cls, name):
        cls.names.add(name)

    @classmethod
    def _new_name(cls):
        return (f'{choice(cls.LETTERS)}'
                f'{choice(cls.LETTERS)}'
                f'{choice(cls.NUMBERS)}'
                f'{choice(cls.NUMBERS)}'
                f'{choice(cls.NUMBERS)}')

    def reset(self):
        Robot.names.discard(self._name)
        self._name = None
