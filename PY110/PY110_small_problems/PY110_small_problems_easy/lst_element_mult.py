# def multiply_elements(lst1, lst2):
#     return [lst1[idx] * lst2[idx] for idx
#             in range(len(lst1))]

def multiply_elements(lst1, lst2):
    return [a * b for a, b in zip(lst1, lst2)]

print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]