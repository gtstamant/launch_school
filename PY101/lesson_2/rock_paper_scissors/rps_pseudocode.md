# Casual Pseudocode

Begin program.

Collect user choice:
- Print request for user choice of rock, paper, or scissors to terminal
- Collect input from user
- Validate input
- - While input invalid, continue to request input

Generate computer choice
- Choose randomly from rock, paper, and scissors

Determine and display winner
- Compare user and computer choices
- Print winner to terminal

# Subprocess Considerations

Compare user and computer choices:

There are 9 (3 ** 3) basic outcomes.
Can these be conceptualized as a matrix?

Rock 1
Paper 2
Scissors 3

2 3 4
3 4 5
4 5 6

Not all sums are unique.
More complex matrix

victory_matrix:
[
(1, 1) (1, 2) (1, 3) # Wins +1, loses +2;   tie     loss    win
(2, 1) (2, 2) (2, 3) # Loses -1, wins +1    win     tie     loss
(3, 1) (3, 2) (3, 3) # Wins -2, loses -1    loss    win     tie
]

(r, p) (r, s)
(p, r) (p, s)
(s, 1) (s, p)

Logic:

victory_matrix[1], [5], [9] = tie
victory_matrix[3], [4], [8] = a wins
victory_matrix[2], [6], [7] = b wins
