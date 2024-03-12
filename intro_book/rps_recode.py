import os
import random

VALID_MOVES = ('paper', 'rock', 'scissors')

WINNING_COMBOS = (
    ['paper', 'rock'],
    ['rock', 'scissors'],
    ['scissors', 'paper'],
)

def get_user_move():
    print('Please input move:')
    move = input().lower()
    while not validate_input(move):
        print("Sorry, that's not a valid move. Try again.")
        move = input().lower()
    move = convert_abreviation(move)
    return move

def validate_input(move):
    abreviated_moves = [move[0] for move in VALID_MOVES]
    if move in abreviated_moves or move in VALID_MOVES:
        return True
    return False

def convert_abreviation(move):
    abreviated_moves = {move[0]: move for move in VALID_MOVES}
    if len(move) == 1:
        return abreviated_moves[move]
    return move

def get_computer_move():
    return random.choice(VALID_MOVES)

def determine_outcome(user_move, computer_move):
    if [user_move, computer_move] in WINNING_COMBOS:
        return 'win'
    if user_move == computer_move:
        return 'tie'
    return 'loss'

def display_score(score_dict):
    for key, value in score_dict.items():
        print(f'The {key} has a record of {value}')

def calculate_rounds(score_dict):
    for value in score_dict.values():
        if value.count('win') == 3:
            return True

def play_round():
    player_move = get_user_move()
    comp_move = get_computer_move()
    return determine_outcome(player_move, comp_move)

def best_of_five():
    score = {
        'player': [],
        'computer': [],
    }

    while not calculate_rounds(score):
        outcome = play_round()

        if outcome == 'win':
            score['player'].append('win')
            score['computer'].append('loss')
        elif outcome == 'loss':
            score['player'].append('loss')
            score['computer'].append('win')
        else:
            score['player'].append('tie')
            score['computer'].append('tie')

        display_score(score)

best_of_five()
