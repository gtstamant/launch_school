import random
import copy
import re
import os

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
FACE_VALUES = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
RANKS = [num for num in range(2, 11)] + [key for key in FACE_VALUES.keys()]
INITIAL_HAND_SIZE = 2
VALID_MOVES = ['hit', 'stay', 'h', 's']
USER_DECISION = ['yes', 'no', 'y', 'n']
HIGH_ACE_VALUE = 11
LOW_ACE_VALUE = 1
MAX_HAND = 21
DEALER_MAX = 17

def prompt(message): # Better name? print_w_arrow
    print(f'==> {message}')

def clear_screen():
    os.system('clear')

def initialize_deck():
    return [{f'{rank} of {suit}': rank} if isinstance(rank, int)
     else {f'{rank} of {suit}': FACE_VALUES[rank]}
     for suit in SUITS
     for rank in RANKS]

def deal_hands(deck):
    player_hand = []
    dealer_hand = []
    
    shuffled_deck = random.sample(deck, k=len(deck))
    for card in range(INITIAL_HAND_SIZE * 2):
        if card % 2 == 0:
            player_hand.append(shuffled_deck.pop())
        else:
            dealer_hand.append(shuffled_deck.pop())

    return shuffled_deck, player_hand, dealer_hand

def hit(deck, hand):
    hand.append(deck.pop())

def split_hand(hand): # get_aces_and_remainder; nested function w/below
    hand_ex_aces, aces = [], []
    for card_info in hand:
        for card in card_info.keys():
            if re.search('ace', card, flags=re.I):
                aces.append(card_info)
            else:
                hand_ex_aces.append(card_info)

    return hand_ex_aces, aces

def get_hand_value(hand):
    hand_ex_aces, aces = split_hand(hand)
    value_ex_aces      = sum(value for card_info in hand_ex_aces
                            for value in card_info.values())
    ace_values         = sum(value for card_info in aces
                            for value in card_info.values())

    while aces and value_ex_aces + ace_values > MAX_HAND:
        for ace_info in aces:
            for ace, value in ace_info.items():
                if value == HIGH_ACE_VALUE:
                    ace_info[ace] = LOW_ACE_VALUE
                    ace_values -= (HIGH_ACE_VALUE - LOW_ACE_VALUE)
        
        if HIGH_ACE_VALUE not in ace_info.values():
            break

    return value_ex_aces + ace_values

def is_bust(hand):
    return get_hand_value(hand) > MAX_HAND

def is_valid_move(user_move): # Change name as not boolean
    return user_move in VALID_MOVES     

def prompt_player_move(): # Need to update this!!!
    while True:
        prompt('Would you like to hit or stay?')
        user_input = input().casefold()
        
        if is_valid_move(user_input):
            return user_input[0]
        prompt("Sorry, that's not a valid move! Try again:")

def display_hands(player_hand, dealer_hand, final=False):
    player_cards = [card for card_info in player_hand # Extract this logic out into nested function
                    for card in card_info.keys()]
    dealer_cards = [card for card_info in dealer_hand
                   for card in card_info.keys()]
    print(f"Your hand:   {', '.join(player_cards[:-1])}" 
            f"{',' if len(player_cards) > 2 else ''} and {player_cards[-1]} ")
    
    if not final:
        print(f"Dealer hand: {', '.join(dealer_cards[1:])}"
               f"{',' if len(dealer_cards) > 2 else ''} and ? of ?")
    else:
        print(f"Dealer hand: {', '.join(dealer_cards[:-1])}"
               f"{',' if len(dealer_cards) > 2 else ''} and {dealer_cards[-1]}")
    print('')

def player_turn(deck, player_hand, dealer_hand):
    clear_screen()
    while get_hand_value(player_hand) != MAX_HAND:
        if is_bust(player_hand):
            break
        
        display_hands(player_hand, dealer_hand)
        prompt_hint(deck, player_hand, dealer_hand)
        # sim_depth = int(input('Need a hint? Set your desired simulation depth: '))
        # if sim_depth: # need to fix, made easy for testing
        #     run_simulation(deck, player_hand, dealer_hand, sim_depth)
        #     input('To return to the game, press [enter]')

        clear_screen()
        prompt('As a reminder, here are your cards:\n')
        display_hands(player_hand, dealer_hand)

        if prompt_player_move() == 'h':
            os.system('clear')
            prompt("You've chosen to hit! Good luck.\n")
            hit(deck, player_hand)
        else:
            os.system('clear')
            prompt("You've chosen to stay! Dealer's move.")
            prompt('Press [enter] to continue')
            input()
            return player_hand
    return player_hand

def dealer_turn(deck, dealer_hand, player_hand):
    
    def dealer_hits(deck, hand):
        while get_hand_value(hand) < DEALER_MAX:
            hit(deck, hand)

        return hand
    
    if not is_bust(player_hand):
        dealer_hand = dealer_hits(deck, dealer_hand)

    return dealer_hand

def get_outcome(player_hand, dealer_hand):
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    
    if is_bust(player_hand):
        return 'Dealer wins: Player went bust'
    if is_bust(dealer_hand): 
        return 'Player wins: Dealer went bust'
    if dealer_value > player_value:
        return f'Dealer wins {dealer_value} to {player_value}'
    if player_value > dealer_value:
        return f'Player wins {player_value} to {dealer_value}'

    return "It's a tie"

def display_winner(outcome, player_hand, dealer_hand):
    os.system('clear')
    prompt(f'{outcome}! Here are the final hands:\n')
    display_hands(player_hand, dealer_hand, True)

def get_hint(simulation_data): # Do I need this one?
    pass

def simulate_player_hand(simulated_deck, simulated_hand, hit_to_num):
    while get_hand_value(simulated_hand) < hit_to_num:
        hit(simulated_deck, simulated_hand)

    return simulated_hand

def play_sim_round(sim_deck, sim_player, sim_dealer, hit_to_num):
    sim_player_hand = simulate_player_hand(sim_deck, sim_player, hit_to_num)
    sim_dealer_hand = dealer_turn(sim_deck, sim_dealer, sim_player)
    sim_outcome = get_outcome(sim_player_hand, sim_dealer_hand)

    return sim_outcome

def run_simulation(deck, player_hand, dealer_hand, sim_depth):
    sim_results = {}
    current_total = get_hand_value(player_hand)

    for hit_to_num in range(current_total, 21):
        for _ in range(sim_depth):
            
            sim_deck   = copy.deepcopy(deck)
            sim_player = copy.deepcopy(player_hand)
            sim_dealer = copy.deepcopy(dealer_hand)
            
            random.shuffle(sim_deck)
            sim_outcome = play_sim_round(sim_deck, sim_player, sim_dealer, hit_to_num)

            if sim_outcome[0] == 'P':
                sim_results[hit_to_num] = sim_results.get(hit_to_num, 0) + 1
    
    win_ratios = {key: (total_wins / sim_depth)
                  for key, total_wins in sim_results.items()}

    display_sim_results(win_ratios, current_total, sim_depth)

def display_sim_results(simulation_results, current_hand, sim_depth): # nest in the above
    clear_screen()
    prompt(f'Simulation results with {sim_depth} iterations')
    for key, win_ratio in simulation_results.items():
        if key == current_hand:
            print(f'Staying at {key} has a {win_ratio * 100:.2f}% win rate.')
        else:
            print(f'Hitting to {key} has a {win_ratio * 100:.2f}% win rate.')
    
    best_choice = max(simulation_results, key=simulation_results.get)
    print('\nAt this point in the game, the optimal strategy is to '
          f"{'stay' if best_choice == current_hand else 'hit'}.\n")

def prompt_user_decision():
    while True:
        decision = input().casefold()
        if is_valid_decision(decision):
            return decision[0]
        print('Sorry, please input [y/n]!')

def is_valid_decision(user_input):
    return user_input in USER_DECISION

def prompt_sim_depth():
    print('How many iterations would you like to simulate?\n'
          'Please choose an number between 100 and 10,001.')
    while True:
        sim_depth = input()
        if is_valid_sim_depth(sim_depth):
            return int(sim_depth)
        print('\nSorry, you need to input an integer between 100 and 10,000.')

def is_valid_sim_depth(depth):
    return depth.isdigit() and (99 < int(depth) < 10001)

def prompt_hint(deck, player_hand, dealer_hand):
    prompt('Need a hint? Do you want to run a simulation? [y/n]\n')

    decision = prompt_user_decision()
    if decision == 'y':

        clear_screen()
        sim_depth = prompt_sim_depth()            
        run_simulation(deck, player_hand, dealer_hand, sim_depth)

        input('To return to the game, press [enter]')
        clear_screen()
        prompt('As a reminder, here are your cards:\n')
        display_hands(player_hand, dealer_hand)

def play_round(deck, player_hand, dealer_hand):
    player_hand = player_turn(deck, player_hand, dealer_hand)
    dealer_hand = dealer_turn(deck, dealer_hand, player_hand)
    outcome = get_outcome(player_hand, dealer_hand)
    
    return outcome, player_hand, dealer_hand

def prompt_play_again():
    prompt('Would you like to play again?')
    return prompt_user_decision()

def play_multiple_rounds():
    while True:
        deck = initialize_deck()
        prompt("Cards are dealt! Press [enter] to play.")
        input()

        deck, player_hand, dealer_hand = deal_hands(deck)
        outcome, player_hand, dealer_hand = play_round(deck, player_hand, dealer_hand)
        display_winner(outcome, player_hand, dealer_hand)
        
        if prompt_play_again() == 'n':
            prompt('Thanks for playing!')
            break
        
        clear_screen()

def play_twenty_one():
    clear_screen()
    prompt('Welcome to Twenty One!\n') # Extract out the prompts
    play_multiple_rounds() # Display final outcome?


play_twenty_one()