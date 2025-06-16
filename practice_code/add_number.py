import square

numbers = []

def add_number(value):
    numbers.append(value)

def get_numbers():
    return numbers.copy()

def sum_of_squares():
    return sum(square(number) for number in get_numbers())