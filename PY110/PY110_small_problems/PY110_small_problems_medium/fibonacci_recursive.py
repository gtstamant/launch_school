"""
## Problem:

Write a recursive function that computes the `nth` fibonacci
number

Explicit requirements:
- Must be implemented recursively
- Base case at 1, 2 should return 1
- F(n) = F(n - 1) + F(n - 2)

## Examples:
- See problem spec

## Data structure
- None needed

## Algorithim

1. If `n` == 1 or `n` == 2
    - return 1
2. Else return Fib(n - 2) + Fib(n - 1)

"""

def fibonacci(n):
    if n <= 2:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True