# def triangle(angle1, angle2, angle3):
#     angles = sorted([angle1, angle2, angle3])

#     def is_valid():
#         if sum(angles) == 180 and 0 not in angles:
#             return True
#         return False
    
#     def get_type():
#         if 90 in angles:
#             return 'right'
#         if angles[2] > 90:
#             return 'obtuse'
#         return 'acute'
    
#     if is_valid():
#         return get_type()
#     return 'invalid'
    
# def triangle(angle1, angle2, angle3):
#     angles = [angle1, angle2, angle3]

#     if sum(angles) != 180 or 0 in angles:
#         return 'invalid'
#     if 90 in angles:
#         return 'right'
#     if all([angle < 90 for angle in angles]):
#         return 'acute'
    
#     return 'obtuse'

def triangle(angle1, angle2, angle3):
    angles = sorted([angle1, angle2, angle3])

    if sum(angles) != 180 or 0 in angles:
        return 'invalid'
    if 90 in angles:
        return 'right'
    if angles[2] > 90:
        return 'obtuse'
    
    return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
    

