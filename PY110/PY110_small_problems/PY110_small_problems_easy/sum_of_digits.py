# def sum_digits(integer):
#     dig_list = list(str(integer))
#     return sum([int(dig) for dig in dig_list])

# def sum_digits(integer):
#     total = 0
#     while integer > 0:
#         total += integer % 10
#         integer //= 10
    
#     return total

# def sum_digits(integer):
#     total = 0
    
#     while integer > 0:
#         integer, remainder = divmod(integer, 10)
#         total += remainder

#     return total

def sum_digits(integer):
    digits = [int(digit) for digit in str(integer)]
    return sum(digits)

print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45