import random
import math

MAX_PLAYER = 'X'
MIN_PLAYER = 'O'

WINNING_COMBINATIONS = [
    'XXX??????',
    'X??X??X??',
    'X???X???X',
    '?X??X??X?',
    '??X?X?X??',
    '???XXX???',
    '??????XXX',
]

X = 'X'
O = 'O'

def generate_board():
    board = {}
    for num in range(1, 10):
        board[num] = '0'
    return board

def update_game_state(player, game_state, move):
    try:
        if game_state[move] == '0':
            game_state[move] = player
    except KeyError:
        pass
    return game_state

def display_board(game_state):
    board_representation = []
    for value in game_state.values():
        board_representation.append(value)
    str_representation = ''.join(board_representation)
    print(str_representation[:3] + '\n' 
          + str_representation[3:6] + '\n' 
          + str_representation[6:])
    
def is_win(player, game_state):
    pattern_check = ['?' if value != player else 'X'
                     for value in game_state.values()
                     ]
    pattern_check_str = ''.join(pattern_check)
    if pattern_check_str in WINNING_COMBINATIONS:
        return True

def is_valid_move(player):
    if player in [X, O]:
        return True

def get_computer_move(game_state):
    while True:
        move = random.choice(list(range(1, 10)))
        print(move)
        if game_state[move] == '0':
            return move

def get_player_move():
    print('Enter your move: ')
    move = int(input())
    return move

def which_player(game_state):
    current_state = list(game_state.values())
    if current_state.count('X') > current_state.count('O'):
        return 'O'
    return 'X'

def all_possible_moves(game_state):
    possible_moves = [
        move[0] for move in game_state.items()
        if move[1] == '0'
    ]
    return possible_moves

def is_game_over(game_state):
    for player in ['X', 'O']:
        if is_win(player, game_state):
            return True
    if len(all_possible_moves(game_state)) == 0:
        return True

def game_value(game_state):
    if is_win(MAX_PLAYER, game_state):
        return 1
    if is_win(MIN_PLAYER, game_state):
        return -1
    return 0

def maximum_value(game_state):
    if is_game_over(game_state):
        return game_value(game_state)
    current_value = -(math.inf)
    for move in all_possible_moves(game_state):
        current_value = max(current_value, minimum_value(update_game_state('O', game_state, move)))
    return current_value

def minimum_value(game_state):
    if is_game_over(game_state):
        return game_value(game_state)
    current_value = math.inf
    for move in all_possible_moves(game_state):
        current_value = min(current_value, maximum_value(update_game_state('X', game_state, move)))
    return current_value

def get_computer_move_2(game_state):
    best_move, best_move_value = None, math.inf
    for move in all_possible_moves(game_state):
        value = minimum_value(update_game_state('O', game_state, move))
        if value < best_move_value:
            best_move, best_move_value = move, value
    return best_move

def play_game():
    board = generate_board()
    while True:   
        display_board(board)
        current_turn = which_player(board)
        match current_turn:
            case 'X':
                update_game_state('X', board, get_player_move())
            case 'O':
                update_game_state('O', board, get_computer_move_2(board))
        if is_win(current_turn, board):
            break

play_game()