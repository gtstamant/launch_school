"""
1. Display Board

## Problem:

Display a tic-tac-toe board based on a current game state

Input: Current game state
Output: Display a representation of a tic-tac-toe board to the console

## Example:

     |     |
     |     |
     |     |
-----+-----+-----   
     |     |
     |     |
     |     |
-----+-----+-----  
     |     |
     |     |
     |     |

2, 3
     
## Data structure:
- Dictionary with tuples (x, y) to keep track
of current moves

## Algorithm:
- For each row in the height of the total board
    - If row 2, 6, 10 ((space height + 1) / 2)
        - Check if move
            - Add appropriate "X", "O", or " "
    - If row 4, 8 (space height + 1) 
        - Generate "----+..." pattern
    - Otherwise (row 1, 3, 5, 7, 9, 11 (other rows)
        - Generate "     |..." pattern

Implementation notes:
- Width: Space width * num spaces + bar width * num spaces - 1
    - Space width: 5
    - Bar width: 1
- Height:
    - Space height: 3
    - Bar height: 1


2. Update game state
    - User mark square
    - Computer mark square

** Subprocess: user choose square **

- Prompt user to choose an open square
- Take user input
    - Check whether move is valid
- Update and display board

4. Check for winner

5. Check if board full



"""
import copy
import re
import os

X = 'X'
O = 'O'
BOARD_SPACES = 3
SPACE_HEIGHT = 3
BAR_SIZE = 1

def initialize_board():
    board = {}

    for i in range(1, 4):       # Coordinates (x, y) from 1-3 more intuitive
        for j in range(1, 4):
            board[(i, j)] = ' '

    return board

def display_board(board):
    os.system('clear')
    board_height = ((SPACE_HEIGHT * BOARD_SPACES) + 
                    (BAR_SIZE * (BOARD_SPACES) - 1))
    
    prompt(f"You are {X}. Computer is {O}.")
    for line in range(1, board_height + 1): # Adding 1 makes calculations easier
        if line % (SPACE_HEIGHT + 1) == 0:
            print('-----+-----+-----')
        
        elif line == 2:
            print(f'  {board[(1, 1)]}  |  {board[(2, 1)]}  |  {board[(3, 1)]} ')
        
        elif line == 6:
            print(f'  {board[(1, 2)]}  |  {board[(2, 2)]}  |  {board[(3, 2)]} ')
        
        elif line == 10:
            print(f'  {board[(1, 3)]}  |  {board[(2, 3)]}  |  {board[(3, 3)]} ')
            
        else:
            print('     |     |     ')
    print('')

def update_board(board, move):
    updated_board = copy.deepcopy(board)
    updated_board[move] = which_player(board)
    
    return updated_board

def which_player(board):
    total_x = sum([1 for square in board.values() if square == 'X'])
    total_o = sum([1 for square in board.values() if square == 'O'])

    if total_x > total_o:
        return O
    else:
        return X

def get_possible_moves(board):
    return [move for move in board.keys()
                      if board[move] == ' ']

def is_valid_move(board, move_coordinates):
    return move_coordinates in get_possible_moves(board)

def prompt(message):
    print(f'==> {message}')

def get_user_move(board):
    
    def convert_str_move(str_move):
        move = tuple([int(char) for char in str_move
                      if char.isdigit()])
        return move
       
    prompt('Please choose an open square!')
    user_move = convert_str_move(input())

    while not is_valid_move(board, user_move):
        prompt("That's not a valid move! Try again.")
        user_move = convert_str_move(input())
    
    return user_move
    
def is_there_a_winner(board):
    winning_combos = [
        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],
        [(1, 1), (2, 2), (3, 3)],
        [(3, 1), (2, 2), (1, 3)],
    ]

    for combo in winning_combos:
        moves = [board[move] for move in combo]
        if len(set(moves)) == 1 and ' ' not in moves:
            return moves[0]
        
def is_game_over(board):
    if is_there_a_winner(board) or not get_possible_moves(board):
        return True

def game_value(game_state):
    winner = is_there_a_winner(game_state)
    
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0

def get_max_value(game_state):
    if is_game_over(game_state):
        return game_value(game_state)
    
    value = -10
    for move in get_possible_moves(game_state):
        value = max(value, get_min_value(update_board(game_state, move)))
    return value

def get_min_value(game_state):
    if is_game_over(game_state):
        return game_value(game_state)
    
    value = 10
    for move in get_possible_moves(game_state):  
        value = min(value, get_max_value(update_board(game_state, move)))
    return value

def minimax(game_state):
    player = which_player(game_state)
    move_values = {}
    possible_moves = get_possible_moves(game_state)
    if not possible_moves:
        return None
    
    if player == 'X':
        for move in possible_moves:
            move_values[move] = get_min_value(update_board(game_state, move))
    else:
        for move in possible_moves:
            move_values[move] = get_max_value(update_board(game_state, move))
        
        return min(move_values, key=move_values.get)

def play_tic_tac_toe():
    while True:
        board = initialize_board()

        while not is_game_over(board):
            display_board(board)
            player_move = get_user_move(board)
            board = update_board(board, player_move)
            display_board(board)
            try:
                computer_move = minimax(board)
                board = update_board(board, computer_move)
                display_board(board)
            except IndexError:
                print("It's a tie!")
                break

        print(f'{is_there_a_winner(board)} wins'
            if is_there_a_winner(board)
            else "It's a tie")
        
        prompt('Play again? [y/n]')
        user_input = input()
        if re.search(r'n(|o)', user_input, flags=re.I):
            prompt('Thanks for playing!')
            break
        
play_tic_tac_toe()