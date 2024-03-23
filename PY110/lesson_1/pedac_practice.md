## Problem ##

** Restate Problem** 

Given a number of blocks, calculate the number of remaining blocks
after building the tallest possible valid structure

** Questions **

- What does it mean for one block to support another block?
- Are all blocks the same size?
- Are there constraints on the width/length of the structure?
    - Is a lower layer valid if it has more blocks than it needs?
    - Will there always be left-over blocks?
- I presume no partial blocks?


** Inputs and Outputs **

Input: an integer, represents number of blocks
Output: an integer, represents remaining blocks after building tallest possible structure

** Rules ** 

Explicit rules:
- Structures are built with blocks:
    - Blocks are cubes
    - Cubes are six-sided, have square faced, and have equal lengths on all sides
- Top layer must be a single block
- Each block on higher layer must be supported by four blocks on lower layer
- Blocks on lower layer can support more than one block on an upper layer
- No gaps between blocks

Implicit rules:
- No partial blocks
- Layers should tend towards squares (equal length on all sides) for highest possible structure
    - Layer number (counting down from top) should match number of blocks on side of structure, e.g. layer 3 has 3 blocks per side
    - Number of blocks in a layer is layer number ** 2

## Examples and Test Cases ##

Further thoughts:
- A single block is a valid layer
- A layer with more than one block that does not support an upper block is considered an invalid layer
    - Valid layers are mathematically equivalent to the sums of series of squares, e.g. (1 * 1 )+ (2 * 2) + (3 * 3) + ... + (n * n)
- There will not always be leftover blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

## Data Structure ##

Programmatic solution:
- Nested list
    - Outer list representing the structure
    - Inner lists representing each layer

[
    ['b'],
    ['b', 'b' ,'b', 'b'],
    ...
]

Mathematical solution:
- List to hold squares and keep track of sums?

## Algorithm ##

<!-- Explicit rules:
- Structures are built with blocks:
    - Blocks are cubes
    - Cubes are six-sided, have square faced, and have equal lengths on all sides
- Top layer must be a single block
- Each block on higher layer must be supported by four blocks on lower layer
- Blocks on lower layer can support more than one block on an upper layer
- No gaps between blocks

Implicit rules:
- No partial blocks
- Layers should tend towards squares (equal length on all sides) for highest possible structure
    - Layer number (counting down from top) should match number of blocks on side of structure, e.g. layer 3 has 3 blocks per side
    - Number of blocks in a layer is layer number ** 2 -->

1. Start with
    - 'num blocks' is equal to input
    - 'sum squares' is equal to empty list
    - 'layer' equal to 1

2. While sum of 'sum squares' is less than 'num blocks'
    - Append 'layer' * 'layer' to 'sum squares'
    - Increment 'layer' by plus one

3. Return 
    - if 'sum squares' = 'num blocks'
        - return 0
    - if 'sum squares' does not equal 'num blocks'
        - return 'num blocks' - (sum of 'sum squares' excluding the final member)

Example:
Given 0:
Loop does not execute
returns 0

Given 1:

Loop:
- 1 [1]
returns 0

Given 2:
Loop
- 1 [1] 
- 2 [1, 4] sum = 5

Returns 2 - 1 = 1

Given 4:
Loop
- 1 [1]
- 2 [1, 4] sum = 5

Returns 4 - 1 = 3

Given 5:
Loop
- 1 [1]
- 2 [1, 4] sum = 5

Return 0

Given 6:

Loop:
- 1 [1] sum = 1
- 2 [1, 4] sum = 5
- 3 [1, 4, 9] sum = 14

Leftovers equals blocks - (sum of members of list excluding last member) 
 


** Test Cases **
<!-- print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True -->