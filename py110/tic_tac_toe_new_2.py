import copy
from pprint import pp

EMPTY = None
X = 'X'
O = 'O'

def generate_board(): # Could redo as dictionary with tuple keys?
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]

def display_board(game_state):
    display_state = copy.deepcopy(game_state)
    for row_num, row in enumerate(game_state):
        for square_num, square in enumerate(row):
            if square == None:
                display_state[row_num][square_num] = ' - '
            else:
                display_state[row_num][square_num] = f' {square} '

    print(
        f'~~~~~~~~~~~~~~~~~~~~\n'
        f'{display_state[0]}\n'
        f'{display_state[1]}\n'
        f'{display_state[2]}\n'
        f'~~~~~~~~~~~~~~~~~~~~')

def get_possible_moves(game_state):
    possible_moves = set()
    for row_num, row in enumerate(game_state):
        for move_num, move in enumerate(row):
            if move == EMPTY:
                possible_moves.add((row_num, move_num))
    return possible_moves

def which_player(game_state):
    num_x = sum(row.count('X') for row in game_state)
    num_o = sum(row.count('O') for row in game_state)

    if num_x > num_o:
        return O
    return X

def update_game_state(game_state, move):
    if move not in get_possible_moves(game_state):
        raise ValueError
    
    new_board = copy.deepcopy(game_state)
    new_board[move[0]][move[1]] = which_player(game_state)
    return new_board

def is_winner(game_state):
    for row in game_state:
        if len(set(row)) == 1 and EMPTY not in row:
            return row[0]
    
    for index in range(len(game_state[0])):
        if game_state[0][index] != EMPTY:
            player = game_state[0][index]
            if player == game_state[1][index] and player == game_state[2][index]:
                return player
    
    if game_state[0][0] != EMPTY:
        player = game_state[0][0]
        if player == game_state[1][1] and player == game_state[2][2]:
            return player
    
    if game_state[0][2] != EMPTY:
        player = game_state[0][2]
        if player == game_state[1][1] and player == game_state[2][0]:
            return player

def is_game_over(game_state):
    if is_winner(game_state) or not get_possible_moves(game_state):
        return True

def game_value(game_state):
    winner = is_winner(game_state)
    
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
        value = max(value, get_min_value(update_game_state(game_state, move)))
    return value

def get_min_value(game_state):
    if is_game_over(game_state):
        return game_value(game_state)
    
    value = 10
    for move in get_possible_moves(game_state):  
        value = min(value, get_max_value(update_game_state(game_state, move)))
    return value

def minimax(game_state):
    player = which_player(game_state)
    move_values = {}
    possible_moves = get_possible_moves(game_state)
    if not possible_moves:
        return None
    
    if player == 'X':
        for move in possible_moves:
            move_values[move] = get_min_value(update_game_state(game_state, move))
    else:
        for move in possible_moves:
            move_values[move] = get_max_value(update_game_state(game_state, move))
        
        return min(move_values, key=move_values.get)

def is_valid_move(game_state, move):
    if move in get_possible_moves(game_state):
        return True

def get_player_move(game_state):
    
    def string_tuple_conversion(input_string):
        move = [int(num) for num in input_string 
                if num.isdigit() ]
        return tuple(move)
        
    print('Please input your move in the form (X, Y).')
    player_move = string_tuple_conversion(input())
    while not is_valid_move(game_state, player_move):
        print("Sorry, that's not a valid move! Try again.")
        player_move = input()
    return player_move

board = generate_board()
display_board(board)

while not is_game_over(board):
    player_move = get_player_move(board)
    board = update_game_state(board, player_move)
    display_board(board)
    try:
        computer_move = minimax(board)
        board = update_game_state(board, computer_move)
        display_board(board)
    except ValueError:
        print("It's a tie!")
        break