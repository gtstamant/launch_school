"""
Problem:

Write a function that takes a 3x3 matrix as an argument and
returns the transposition of that matrix

Input: nested list; a list with three lists nested inside it
Output: a new set of nested lists representing a 3x3 matrix

Explicit requirements:
- Transposition means exchanging the rows and columns in order
- The function should not mutate the original matrix
- The function should not use external libraries

Implicit requirements:
- You may assume a valid input

Examples:
- See problem spec

Data structure:
- A nested list

Algorithm:
- Initialize `transposed matrix` to an empty list
    - Calculate the length of `input` list and set to `outer length`
    - Initialize `outer length` number of empty lists within `transposed matrix`
- Calculate the length of one of the `nest lists` and set to `inner length`
- Loop through `inner length` number of indices
    - For each index, loop through `outer length` number of lists
    - Add the number at each index in each nested list to the nested
     lists in `transposed matrix`
- Return `transposed matrix`

Implementation notes:
- Obvious solution for NxN matrix is to use the zip function

[
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

for idx in len(matrix[0]) 
==> 1
==> 2
==> 3

[sub_list[idx] for sublist in matrix]
[1, 4, 3]
[5, 7, 2]...

[[sub_list[idx] for sublist in matrix] for idx in len(matrix[0])

"""


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

def transpose(matrix):
    return [[sublist[idx] for sublist in matrix] for idx in range(len(matrix[0]))]

# def transpose(matrix):
#     transposed_matrix = []
#     for row in matrix:
#         transposed_matrix.append([])
    
#     inner_len = len(matrix[0])
#     for idx in range(inner_len):
#         for row in matrix:
#             transposed_matrix[idx].append(row[idx])
    
#     return transposed_matrix

# def transpose(matrix):
#     zipped_args = zip(*matrix)
#     new_matrix = [list(tup) for tup in zipped_args]

#     return new_matrix

# def transpose(matrix):
#     return [[sub[i] for sub in matrix] for i in range(len(matrix))]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True