import os
import random
import json

VALID_MOVES = ['rock',
               'paper',
               'scissors',
               'lizard',
               'spock',
               ]

with open('rps.json', 'r') as display_data:
    display_messages = json.load(display_data)

def get_user_move():
    print(f'Please choose one: {", ".join(VALID_MOVES)}.\n')
    user_choice = input().lower()
    while user_choice not in VALID_MOVES:
        print(f"Oops, that's not a valid move."
              f"Please choose one: {', '.join(VALID_MOVES)}.\n")
        user_choice = input().lower()
    return user_choice

def get_computer_move():
    return random.choice(VALID_MOVES)

def determine_tie(player_move, computer_move):
    if player_move == computer_move:
        return True
    return False

def check_player_wins(player_move, computer_move):
    match player_move:
        case 'rock' if computer_move in ['scissors', 'lizard']:
            return True
        case 'paper' if computer_move in ['rock', 'spock']:
            return True
        case 'scissors' if computer_move in ['paper', 'lizard']:
            return True
        case 'spock' if computer_move in ['rock', 'scissors']:
            return True
        case 'lizard' if computer_move in ['spock', 'paper']:
            return True
    return False

def determine_outcome(player_move, computer_move):
    if determine_tie(player_move, computer_move):
        return 'tie'
    if check_player_wins(player_move, computer_move):
        return 'win'
    return 'loss'

def check_best_of_five(game_results):
    if game_results.count('win') == 3:
        return True
    if game_results.count('loss') == 3:
        return True
    return False

def display_outcome(player_move, computer_move, game_outcome):
    print(f'\nYou chose {player_move} and the computer chose {computer_move}:'
          f' player {display_messages[game_outcome]}.')

def display_current_results(result_list):
    print(f'Your current results are: {", ".join(result_list)}.\n')

def display_final_score(result_list):
    if result_list.count('win') == 3:
        print("You've won best of five!\n")
    else:
        print("You've lost best of five!\n")

def get_user_choice():
    user_choice = input().lower()
    while user_choice not in ['y', 'n', 'yes', 'no']:
        print("Sorry, that's not a valid choice. Please enter [y]/[n]\n")
        user_choice = input().lower()
    return user_choice[0]

def get_replay_choice():
    print('Would you like to play again? Please enter [y]/[n]\n')
    return get_user_choice()

def decide_game_replay(continue_choice):
    if continue_choice == 'y':
        return True
    return False

def get_continue_decision():  # need to fix
    input('Press enter to continue...\n')

def play_game():
    print("Let's play a round of rock, paper, scissors.\n")
    player_move = get_user_move()
    computer_move = get_computer_move()
    outcome = determine_outcome(player_move, computer_move)
    display_outcome(player_move, computer_move, outcome)
    return outcome

def play_best_of_five():
    while True:
        results = []
        os.system('clear')
        print("Welcome to rock, paper, scissors — best of five!\n")

        while not check_best_of_five(results):
            game_result = play_game()
            results.append(game_result)
            display_current_results(results)
            get_continue_decision()
            os.system('clear')

        display_final_score(results)
        replay_choice = get_replay_choice()

        if not decide_game_replay(replay_choice):
            print('Thanks for playing. Goodbye!')
            return False

play_best_of_five()