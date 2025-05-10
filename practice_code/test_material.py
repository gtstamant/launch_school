class TestClass:
    pass

class NoExperienceError(Exception):
    def __init__(self, message="We can't hire without experience!"):
        super().__init__(message)

class Employee:
    def hire(self):
        raise NoExperienceError

class Number:
    pass

class Numeric(Number):
    pass

class Lst:
    def process(self):
        return self