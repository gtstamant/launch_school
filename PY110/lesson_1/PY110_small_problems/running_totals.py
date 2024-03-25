"""
## Problem ##

Given a list of numbers, return a list with the same
number of elements. Each value in the new ist should
reflect the running total from the original list.

Input: A list of numbers
Output: A list of numbers, each element reflects running total of
numbers in the original list

Explicit rules:
- In problem description

Implicit rules:
- First element in new list equals the first element in original list
- An empty list should return an empty list
- A list with one element should return a list
with that same element
- All lists will be comprised of integers only


Questions:
- Should we return a new list or a mutated version of the old list?
- Do we need to worry about input validation?
- Should we expect negative numbers, floats, NaN, or imaginaries?

Examples: 

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

Data structure:

A list (return value)

Algorithm:

1. Take a list of integers 'original list' as input
2. Set variable 'running total' to an empty list
3. Set the first element of 'running total' equal to the first
element in 'original list
4. Starting from the second element in 'original list' go through
each 'current element'
- Add the value of the last 'original list' element to the
'current element' from 'original list
- Append this value to the end of 'running total'
- Stop when you reach the end of 'original list'
5. Return 'running total'

Implementation notes:

1. One could implement by progressive slicing, but computationally expensive

"""

def running_total_1(numbers):
    try:
        run_total = [numbers[0]]
    
        for index in range(1, len(numbers)):
            previous_idx = index - 1
            run_total.append(numbers[index] 
                            + run_total[previous_idx])
        
        return run_total
    
    except IndexError:
        return []
    
# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

"""
numbers = [2, 5, 13]
run_total = [2]

For indexes (1, 2)
    run_total.append(5 + 2) [2, 7]
    run_total.append(13 + 7) [2, 7, 20]


"""

# Slicing solution

def running_total_2(numbers):
    run_total = []
    
    for indx, element in enumerate(numbers):
        try:
            current_value = sum(numbers[:indx + 1])
            run_total.append(current_value)
        except IndexError:
            current_value = sum(numbers)
            run_total.append(current_value)
    
    return run_total

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# Easiest solution

def running_total_3(numbers):
    run_total = []
    total = 0

    for num in numbers:
        total += num
        run_total.append(total)

    return run_total

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# Recursive solution?

def running_total(numbers, run_total):
    if len(numbers) == 1 or len(numbers) == 0:
        run_total.append(numbers[0])
        return run_total
    
    print(sum(running_total(numbers[:-1], run_total)))
    run_total.append(sum(running_total(numbers[:-1], run_total)) + numbers[-1])
    print(run_total)
    return run_total

print(running_total([2, 5, 13], []) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True