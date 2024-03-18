X player tries to get biggest score
O player tries to get smallest score

define function comp_decision which takes current game state as an argument
- evaluates current game state for possible moves
- maximizing player chooses move in possible moves that returns max value
    of 


loops through possible moves, updating game state
    - checks if move results in win or loss
        - if X win return 1
        - if O player can win within one move, return -1
        - else call comp_decision on new game state