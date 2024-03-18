import copy

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

