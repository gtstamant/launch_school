"""
## Problem:
Write a function that takes a matrix as an argument
and returns a new matrix that has been rotated 90 degrees

Input: a nested-list representation of a matrix
Output: a new nested-list representation of the rotated matrix

## Explicit requirements:
- Each row should be transposed as a column
- The Transposition should begin from the bottom row
    - Bottom row to left most column
- The function must handle arbitrary MxN matrices
- The function should not mutate the original matrix

## Implicit requirements:
- Can expect a valid matrix

## Examples:
- See problem spec

## Data structure:
- Nested list

## Algorithm:

Indexing issues:

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

==>

[2][0] => [0][0] // [1][0] => [0][1] // [0][0] => [0][2]
[2][1], [1][1], [0][1]
[2][2], [1][2], [0][2]

transposed = [
    [3, 4, 1],
    [9, 7, 5],
    [6, 2, 8],
]

Outer loop ==> 0, 1, 2
Inner loop ==> 2, 1, 0

loop through: [inner_loop][outer_loop]

Mental model:

1. Start with a matrix made up of nested lists.
2. Build a data structure for the transposed matrix
    - The `n` number of rows in the `rotated matrix` must
    equal the length of the rows in the `initial matrix`.
        - Initialize a new, empty list
        - Append `n` empty lists to it
3. Access the correct elements and append them to the new data structure
4. Return the data structure

** Subprocess **

- Set a range of indices from 0 to `m` (the number of rows in the `initial matrix`)
    - Reverse loop through the `n` lists of the initial matrix
    - Access the `index` element of the `n`th list of the initial matrix
    - Repeat with `n` - 1, - 2 ... '
- After getting to the last list of the initial matrix
    - Increase the index by 1
    - Repeat until index reaches `m`

Implementation notes:
- for `m`: range(len(matrix))
- for `n`: range(len(matrix[0]))
    
"""

def rotate90(matrix):
    rotated = []
    for _ in matrix[0]:
        rotated.append([])
    
    for idx in range(len(matrix[0])):
        for row_num in range(len(matrix) - 1, -1, -1):
            rotated[idx].append(matrix[row_num][idx])
    
    return rotated
        
matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)