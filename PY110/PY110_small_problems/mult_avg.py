def multiplicative_average(lst):
    result = 1
    for num in lst:
        result *= num

    # return f'{result / len(lst):.3f}'
    return round_to_three(result / len(lst))

def round_to_three(num):
    str_num = str(round(num, 3))
    decimal_idx = str_num.find('.')

    while len(str_num[decimal_idx + 1:]) < 3:
        str_num += '0'

    return str_num

# just to see if I can do recursively

# def multiplicative_result(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return (lst[-1] * multiplicative_result(lst[:-1]))

# def multiplicative_average(lst):
#     return f'{multiplicative_result(lst) / len(lst):.03f}'

print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

"""

7.5
'7.5' # '.' index is 1, len of '7.5' is 3
3 - 1 = 2, need to add two 0s
4 - 1
5 - 1

"""