def triangle(side1, side2, side3):

    def is_valid():
        sides = sorted([side1, side2, side3])
        if sum(sides[:2]) > sides[2] and min(sides) > 0:
            return True
        return False
    
    def get_type():
        if side1 == side2 == side3:
            return 'equilateral'
        if side1 == side2 or side1 == side3 or side2 == side3:
            return 'isosceles'
        return 'scalene'
    
    if is_valid():
        return get_type()
    return 'invalid'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == 'invalid')      # True