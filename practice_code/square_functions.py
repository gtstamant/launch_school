# square_functions.py
from numbers_functions import get_numbers

def square(value):
    return value * value

def sum_of_squares():
    return sum(square(number) for number in get_numbers())