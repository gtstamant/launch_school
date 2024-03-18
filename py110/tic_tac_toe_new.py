import math
import copy

EMPTY = None
PLAYERS = ('X', 'O')
CORNER_INDEXES = (0, 2)
X, O = PLAYERS
WINNING_COMBINATIONS = [
    'PPP??????',
    'P??P??P??',
    'P???P???P',
    '?P??P??P?',
    '??P?P?P??',
    '???PPP???',
    '??????PPP',
]

def generate_board(): # Could redo as dictionary with tuple keys?
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]

def get_possible_moves(game_state):
    possible_moves = []
    for row_num, row in enumerate(game_state):
        for move_num, move in enumerate(row):
            if move == EMPTY:
                possible_moves.append((row_num, move_num))
    return possible_moves

def update_game_state(game_state, move, player):
    if move not in get_possible_moves(game_state):
        raise ValueError
    
    new_board = copy.deepcopy(game_state)
    new_board[move[0]][move[1]] = player
    return new_board

def determine_winner(game_state):
    for player in PLAYERS:
        string_representation = ''
        for row in game_state: # write a "get squares" function? Or str-rep?
            for square in row:
                if square == player:
                    string_representation += 'P'
                else:
                    string_representation += '?'
        if string_representation in WINNING_COMBINATIONS:
            return player

def is_game_over(game_state):
    if determine_winner(game_state):
        return True
    for row in game_state:
        if EMPTY in row:
            return None
    return True

def game_value(game_state):
    match determine_winner(game_state):
        case 'X':
            return 1
        case 'O':
            return -1
        case _:
            return 0

def which_player(game_state):
    num_x = sum(row.count('X') for row in game_state)
    num_o = sum(row.count('O') for row in game_state)

    if num_x > num_o:
        return O
    return X

def minimax(game_state):
    
    def get_max(game_state):
        if is_game_over(game_state):
            return game_value(game_state)
        
        value = -math.inf
        for move in get_possible_moves(game_state):
            value = max(value, get_min(update_game_state(game_state, move, X)))
        return value
    
    def get_min(game_state):
        if is_game_over(game_state):
            return game_value(game_state)
        
        value = math.inf
        for move in get_possible_moves(game_state):
            value = min(value, get_max(update_game_state(game_state, move, O)))
        return value
    
    def compute_move_value(game_state, player):
        match player:
            case 'X':
                return get_max(game_state)
            case 'O':
                return get_min(game_state)

    if is_game_over(game_state):
        return None
    
    player = which_player(game_state)
    best_move = []
    for move in get_possible_moves(game_state):
        try:
            value = compute_move_value(update_game_state(game_state, move, X), player)
            if value > best_move[1]:
                best_move[0], best_move[1] = move, value
        except IndexError:
            best_move.append(move)
            best_move.append(compute_move_value(update_game_state(game_state, move, X), player))
    return best_move

    # for move in get_possible_moves(game_state):
    #     try:
    #         value = get_max(update_game_state(game_state, move, X))
    #         if value > best_move[1]:
    #             best_move[0], best_move[1] = move, value
    #     except IndexError:
    #         best_move.append(move)
    #         best_move.append(get_max(update_game_state(game_state, move, X)))
    # return best_move



board = generate_board()
board = update_game_state(board, (0, 0), X)
board = update_game_state(board, (0, 1), O)
print(minimax(board))        
