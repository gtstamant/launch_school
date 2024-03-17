import random

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
    if game_state[move] == '0':
        game_state[move] = player
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

def play_game():
    move_tracker = 'X'
    board = generate_board()
    while True:   
        display_board(board)
        match move_tracker:
            case 'X':
                update_game_state('X', board, get_player_move())
                move_tracker = 'O'
            case 'O':
                update_game_state('O', board, get_computer_move(board))
                move_tracker = 'X'
        if is_win(move_tracker, board):
            break

play_game()