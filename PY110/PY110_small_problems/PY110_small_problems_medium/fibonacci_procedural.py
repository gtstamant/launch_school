"""
## Problem:

Write a function that computes the `nth` Fibonacci number
where n is an argument passed to the function

## Examples:
- See problem spec

## Data structure
- Lists

## Algorithm
- Initialize `fib_seq` as a list with `n` elements set to 1
- Iterate over a sequence of numbers ranging from 3 to `n`
    - Set the element in `fib_seq` at current value of iteration
    to the sum of the elements at indices one and two less
    than the current value
- Return `fib_seq`

"""

def fibonacci(n):
    # fib_seq = [1 for _ in range(n)]

    # for idx in range(2, n):
    #     fib_seq[idx] = fib_seq[idx - 1] + fib_seq[idx - 2]
    
    # return fib_seq[-1]
    if n < 3:
        return 1
    
    current, previous = 1, 1
    for _ in range(2, n):
        current, previous = current + previous, current
    
    return current


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True