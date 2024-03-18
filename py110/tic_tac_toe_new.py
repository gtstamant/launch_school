import copy
from pprint import pp

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
    possible_moves = []
    for row_num, row in enumerate(game_state):
        for move_num, move in enumerate(row):
            if move == EMPTY:
                possible_moves.append((row_num, move_num))
    return possible_moves

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
            return False
    return True

def game_value(game_state):
    winner = determine_winner(game_state)
    
    if winner == X:
        return 1
    if winner == O:
        return -1
    else:
        return 0

def which_player(game_state):
    num_x = sum(row.count('X') for row in game_state)
    num_o = sum(row.count('O') for row in game_state)

    if num_x > num_o:
        return O
    return X

def minimax(game_state):
    
    def get_max_val(game_state):
        if is_game_over(game_state):
            return game_value(game_state)
    
        value = -10
        for move in get_possible_moves(game_state):
            new_state = update_game_state(game_state, move, O)
            if value < get_min_val(new_state):
                value = get_min_val(new_state)
        return value

    def get_min_val(game_state):
        if is_game_over(game_state):
            return game_value(game_state)
        
        value = 10
        for move in get_possible_moves(game_state):
            new_state = update_game_state(game_state, move, X)
            if value > get_max_val(new_state):
                value = get_max_val(new_state)
        return value
    
    player = which_player(game_state)

    moves = {}
    for move in get_possible_moves(game_state):
        test_board = update_game_state(game_state, move, player)
        moves[move] = get_min_val(test_board)
    
    return moves




#     def get_max(game_state):
#         if is_game_over(game_state):
#             return game_value(game_state)
        
#         value = -math.inf
#         move = None
#         for move in get_possible_moves(game_state):
#             value = max(value, get_min(update_game_state(game_state, move, O)))
#         return value
    
#     def get_min(game_state):
#         if is_game_over(game_state):
#             return game_value(game_state)
        
#         value = math.inf
#         for move in get_possible_moves(game_state):
#             value = min(value, get_max(update_game_state(game_state, move, X)))
#         return value
    
#     def compute_move_value(game_state, player):
#         match player:
#             case 'X':
#                 return get_max(game_state)
#             case 'O':
#                 return get_min(game_state)

#     if is_game_over(game_state):
#         return None
    
#     player = which_player(game_state)
#     print(player)
#     best_move = [None, math.inf]
#     for move in get_possible_moves(game_state):
#         value = get_min(update_game_state(game_state, move, player)) # here is the error - 
#         if value < best_move[1]: 
#             best_move[0], best_move[1] = move, value
#     return best_move[0]

board = generate_board()
board = update_game_state(board, (0, 0), X)


display_board(board)
print(is_game_over(board))

pp(minimax(board))

# board = generate_board()
# while not is_game_over(board):
#     display_board(board)
#     player_move = get_player_move(board)
#     print(player_move)
#     board = update_game_state(board, player_move, X)
#     display_board(board)
#     computer_move = minimax(board)
#     board = update_game_state(board, computer_move, O)



