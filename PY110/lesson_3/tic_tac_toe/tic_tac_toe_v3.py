import copy
import os
import random

OPEN_SPACE = ' '
BOARD_SPACES = 3
SPACE_HEIGHT = 3
BAR_SIZE = 1
BOARD_HEIGHT = ((SPACE_HEIGHT * BOARD_SPACES) +
                    (BAR_SIZE * (BOARD_SPACES - 1)))
INPUT_LINE_1 = 2
INPUT_LINE_2 = 6
INPUT_LINE_3 = 10

def prompt(message):
    print(f'==> {message}')

def initialize_board():
    board = {}

    for i in range(1, 4):       # Coordinates (x, y) from 1-3 more intuitive
        for j in range(1, 4):
            board[(i, j)] = ' '

    return board

def which_player(board):
    total_x = sum([1 for square in board.values()
                   if square == 'X'])
    total_o = sum([1 for square in board.values()
                   if square == 'O'])

    if total_x > total_o:
        return 'O'
    else: # Pylint complains, but perhaps more readable?
        return 'X'

def update_board(board, move):
    updated_board = copy.deepcopy(board)
    updated_board[move] = which_player(board)

    return updated_board

def display_board(board, player, computer):
    os.system('clear')

    prompt(f"You are {player}. Computer is {computer}.")
    for line in range(1, BOARD_HEIGHT + 1):
        # Adding 1 makes calculations intuitive
        if line % (SPACE_HEIGHT + 1) == 0:
            print('-----+-----+-----')
        # Pylint complains, but I think keeping on one line aids readability
        elif line == INPUT_LINE_1:
            print(f'  {board[(1, 3)]}  |  {board[(2, 3)]}  |  {board[(3, 3)]} ')
        elif line == INPUT_LINE_2:
            print(f'  {board[(1, 2)]}  |  {board[(2, 2)]}  |  {board[(3, 2)]} ')
        elif line == INPUT_LINE_3:
            print(f'  {board[(1, 1)]}  |  {board[(2, 1)]}  |  {board[(3, 1)]} ')
        else:
            print('     |     |     ')
    print('')

def display_example_board():
    os.system('clear')
    prompt("Moves are indicated by their x, y coordinates:")

    for line in range(1, BOARD_HEIGHT + 1):
        # Adding 1 makes calculations inutitive
        if line % (SPACE_HEIGHT + 1) == 0:
            print('-----+------+-----')
        elif line == INPUT_LINE_1:
            print('1, 3 | 2, 3 | 3, 3 ')
        elif line == INPUT_LINE_2:
            print('1, 2 | 2, 2 | 3, 2 ')
        elif line == INPUT_LINE_3:
            print('1, 1 | 2, 1 | 3, 1 ')
        else:
            print('     |      |     ')
    print('')

def display_instructions():
    os.system('clear')
    prompt('Welcome to tic-tac-toe!\n'
           'The board is arranged like a Cartesian plane. \n'
           'To make your move, input an x and y co-ordinate.\n')

    prompt('Would you like to see the layout '
           'with the move co-ordinates indicated? [y/n]')

    if get_user_yes_no() == 'y':
        display_example_board()

    prompt('Ready to play? If yes, enter [y]. Enter [n] to quit')

    if get_user_yes_no() == 'n':
        prompt("So sorry! I suppose it's game over for now!")
        return None
    else: # Pylint complains, but perhaps more readable?
        return True

def display_win_percentages(win_dict):
    prompt('Would you like to see the current '
           'win/loss/tie record? Enter [y/n].')

    if get_user_yes_no() == 'y':
        os.system('clear')
        total_games = sum(win_dict.values())

        prompt(f"You've played {total_games} "
               f"game{'s' if total_games > 1 else ''}.\n"
               'Win percentages: \n')

        for outcome in win_dict.keys():
            try:
                outcome_percentage = (win_dict[outcome]/total_games) * 100
            except ZeroDivisionError:
                outcome_percentage = win_dict[outcome]
            print(f'{outcome}: {outcome_percentage:.2f}%')

        print('\n')
        prompt('Enter [enter] to continue.')
        input()

def get_user_yes_no():
    user_input = input().casefold()

    while user_input not in ['y', 'yes', 'n', 'no']:
        prompt('Invalid input! Please enter [y/n].')
        user_input = input().casefold()

    return user_input[0]

def get_possible_moves(board):
    return [move for move in board.keys()
                      if board[move] == OPEN_SPACE]

def is_valid_move(board, move_coordinates):
    return move_coordinates in get_possible_moves(board)

def get_user_move(board):

    def convert_move(str_move):
        move = tuple([int(char) for char in str_move
                      if char.isdigit()])
        return move

    prompt('Please choose the co-ordinates of an open square!')
    user_move = convert_move(input())

    while not is_valid_move(board, user_move):
        prompt("That's not a valid move! Remember to use x, y format.")
        user_move = convert_move(input())

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
        if len(set(moves)) == 1 and OPEN_SPACE not in moves:
            return moves[0]

    return None

def is_game_over(board):
    if is_there_a_winner(board) or not get_possible_moves(board):
        return True

    return False

def get_game_value(board):
    winner = is_there_a_winner(board)

    if winner == 'X':
        return 1
    elif winner == 'O': # Pylint complains, but more readable?
        return -1
    else:               # Pylint complains, but more readable?
        return 0

def get_max_value(board, depth, alpha, beta):
    if is_game_over(board):
        return (get_game_value(board), depth + 1)

    value = (-10, -10) # win value and depth value
    for move in get_possible_moves(board):
        value = max(value, get_min_value(update_board(board, move), depth + 1,
                                         alpha, beta))
        if value[0] > beta:
            break
        alpha = max(value[0], alpha)
    return value

def get_min_value(board, depth, alpha, beta):
    if is_game_over(board):
        return (get_game_value(board), depth + 1)

    value = (10, 10)
    for move in get_possible_moves(board):
        value = min(value, get_max_value(update_board(board, move), depth + 1,
                                         alpha, beta))
        if value[0] < alpha:
            break
        beta = min(value[0], beta)
    return value

def minimax(board, alpha=-10, beta=10):
    player = which_player(board)
    move_values = {}
    possible_moves = get_possible_moves(board)
    if not possible_moves:
        return None

    depth_counter = 0 # Track depth to return optimal move with shortest game
    if player == 'X':

        for move in possible_moves:
            move_values[move] = get_min_value(update_board(board, move),
                                              depth_counter, alpha, beta)

        # depth optimization verbose because max() returns worst depth
        max_move = max(move_values, key=move_values.get)
        max_move_value = move_values[max_move][0]

        possible_max_moves = [move for move, value in move_values.items()
                              if value[0] == max_move_value]

        depth_optimized_max = min(possible_max_moves, key=move_values.get)
        possible_max_moves = [move for move, value in move_values.items()
                              if value == move_values[depth_optimized_max]]

        # random choice among optimal moves to add variety
        return random.choice(possible_max_moves)

    else:
        for move in possible_moves:
            move_values[move] = get_max_value(update_board(board, move),
                                              depth_counter, alpha, beta)

        min_move = min(move_values, key=move_values.get)
        min_move_value = move_values[min_move]

        possible_min_moves = [move for move, value in move_values.items()
                            if value == min_move_value]

        return random.choice(possible_min_moves)

def choose_player_order():
    os.system('clear')
    prompt('Would you like to go first? Enter [y] to go first, '
           '[n] to go second.')
    if get_user_yes_no() == 'y':
        return get_user_move, minimax
    return minimax, get_user_move

def get_player_identities(player_move_function):
    if player_move_function == get_user_move:
        user, computer = 'X', 'O'
    else:
        computer, user = 'X', 'O'

    return user, computer

def play_move(board, player1, player2):
    player = which_player(board)
    match player:
        case 'X':
            return player1(board)
        case 'O':
            return player2(board)

def which_player_won(winner, user, computer):
    if winner == user:
        return 'Player'
    elif winner == computer:
        return 'Computer'
    else:
        return 'Tie'

def display_winner(winner):
    if winner != 'Tie':
        print(f'{winner} wins!')
    else:
        print("It's a tie!")

def play_tic_tac_toe():
    win_count = {'Player': 0, 'Computer': 0, 'Tie': 0}
    if not display_instructions():
        return

    while True:
        board = initialize_board()
        player1, player2 = choose_player_order()
        user, computer = get_player_identities(player1)

        while not is_game_over(board):
            display_board(board, user, computer)
            move = play_move(board, player1, player2)
            board = update_board(board, move)

        display_board(board, user, computer)
        winner = which_player_won(is_there_a_winner(board), user, computer)
        display_winner(winner)
        win_count[winner] += 1

        display_win_percentages(win_count)
        prompt('Play again? [y/n]')
        if get_user_yes_no() == 'n':
            prompt('Thanks for playing!')
            return

play_tic_tac_toe()