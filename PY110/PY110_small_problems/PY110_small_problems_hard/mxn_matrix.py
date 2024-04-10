"""
Problem:
Write a function that transposes any MxN matrix
with at least one row and one column

Input: nested list representation of a matrix
Output: a new nested list representation of the transposed matrix

Explicit requirements:
- Must work with any matric of at least one row and one column
- Do not mutate original input

Implicit requirements:
- Can assume a valid matrix input

Examples:
- See problem spec

Data structure:
- Nested list

Algorithm:

1. Mental model

[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

We want to build a nested list structure. We need to take the element 
at each index `n` in each of the nested lists and use those elements 
to populate a nested list at index `m` in the larger list. 
We then need to do the same for `n + 1` and `m + 1`, continuing until we reach
the index `n + x` that corresponds with the length of any of the nested
lists, which should all share the same length.

2. Pseudocode

- Initialize `outer list` to an empty list
- Initialize `n` inner lists; `n` = length of any sublist in matrix
- Loop through the sublists of the original matrix
    - Take the element at the first idx of the first sublist
    - Add it to the first list of the new matrix
    - Continue by moving to the next sublist
    - Continue adding the first element to the first list of the new matrix
    - When last sublist is reached and adding complete
        - Increment the index number by one
    - Continue until index is equal to the length of a list in the original matrix
- Return the new matrix

Implementation Notes:

Matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposed_matrix = [
    [],
    [],
]

"""

# def transpose(matrix):
#     transposed_matrix = []
    
#     for _ in matrix[0]:
#         transposed_matrix.append([])
    
#     for lst_idx in range(len(matrix[0])):
#         for row_idx in range(len(matrix)):
#             transposed_matrix[lst_idx].append(matrix[row_idx][lst_idx])
    
#     return transposed_matrix

def transpose(matrix):
    return [[sublist[idx] for sublist in matrix] 
            for idx in range(len(matrix[0]))]

print(transpose([[1, 2, 3, 4]]))            # [[1], [2], [3], [4]]
print(transpose([[1], [2], [3], [4]]))      # [[1, 2, 3, 4]]
print(transpose([[1]]))                     # [[1]]

print(transpose([[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [3, 7, 8, 6, 2]]))
# [[1, 4, 3], [2, 3, 7], [3, 2, 8], [4, 1, 6], [5, 0, 2]]