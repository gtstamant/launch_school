# def fibonacci(n, memo={}):
#     if n <= 2:
#         return 1
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return memo[n]

# def find_fibonacci_index_by_length(length):
#     n = 0
#     while True:
#         current_fib = fibonacci(n)
#         if len(str(current_fib)) == length:
#             return n
#         n += 1

import sys


def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50_000)
    current, previous = 1, 1
    index = 2
    while len(str(current)) < length:
        current, previous = current + previous, current
        index += 1
    
    return index

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
print(find_fibonacci_index_by_length(10000) == 47847)