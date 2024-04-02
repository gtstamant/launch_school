# def multiply_list(lst):
#     for idx, item in enumerate(lst):
#         lst[idx] *= 2
#     return lst

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]))