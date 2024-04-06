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
ACE_TEST_FORK_MIN = 16

def arrow_print(message):
    print(f'==> {message}')

def clear_screen():
    os.system('clear')

def prompt_user_decision():
    while True:
        decision = input().casefold()
        if is_valid_decision(decision):
            return decision[0]
        print('Sorry, please input [y/n]!')

def is_valid_decision(user_input):
    return user_input in USER_DECISION

def initialize_deck():
    return [{f'{rank} of {suit}': rank} if isinstance(rank, int)
           else {f'{rank} of {suit}': FACE_VALUES[rank]}
           for suit in SUITS
           for rank in RANKS]

def deal_hands(deck):
    player_hand = []
    dealer_hand = []

    shuffled_deck = random.sample(deck, k=len(deck))
    for card_num in range(INITIAL_HAND_SIZE * 2):
        if card_num % 2 == 0:
            player_hand.append(shuffled_deck.pop())
        else:
            dealer_hand.append(shuffled_deck.pop())

    return shuffled_deck, player_hand, dealer_hand

def hit(deck, hand):
    hand.append(deck.pop())

def is_ace(card):
    return re.search('ace', card, flags=re.I)

def split_hand(hand):
    hand_excl_aces, aces = [], []
    for card_info in hand:
        for card in card_info.keys():
            if is_ace(card):
                aces.append(card_info)
            else:
                hand_excl_aces.append(card_info)

    return hand_excl_aces, aces

def get_hand_value(hand):

    def get_card_values(cards):
        return [value for card_info in cards 
               for value in card_info.values()]

    def update_aces(value_ex_aces, ace_values, aces):
        if HIGH_ACE_VALUE not in get_card_values(aces):
            return ace_values

        for card_info in aces:
            for key in card_info:
                if value_ex_aces + ace_values > MAX_HAND:
                    card_info[key] = LOW_ACE_VALUE
                    ace_values = sum(get_card_values(aces))

        return ace_values

    hand_excl_aces, aces = split_hand(hand)
    value_excl_aces      = sum(get_card_values(hand_excl_aces))
    ace_values           = sum(get_card_values(aces))

    updated_ace_values = update_aces(value_excl_aces, ace_values, aces)

    return value_excl_aces + updated_ace_values

def is_bust(hand):
    return get_hand_value(hand) > MAX_HAND

def is_valid_move(user_move):
    return user_move in VALID_MOVES     

def prompt_player_move():
    while True:
        arrow_print('Would you like to hit or stay? Enter [h/s]')
        user_input = input().casefold()

        if is_valid_move(user_input):
            return user_input[0]
        arrow_print("Sorry, that's not a valid move! Try again:")

def display_hands(player_hand, dealer_hand, final=False):

    def get_card_names():
        player_cards = [card for card_info in player_hand
                       for card in card_info.keys()]
        dealer_cards = [card for card_info in dealer_hand
                       for card in card_info.keys()]

        return player_cards, dealer_cards

    player_cards, dealer_cards = get_card_names()

    print(f"Your hand:   {', '.join(player_cards[:-1])}"
            f"{',' if len(player_cards) > 2 else ''} and {player_cards[-1]}. "
            f"Total hand value: {get_hand_value(player_hand)}")

    if not final:
        print(f"Dealer hand: {', '.join(dealer_cards[1:])}"
               f"{',' if len(dealer_cards) > 2 else ''} and ? of ?")
    else:
        print(f"Dealer hand: {', '.join(dealer_cards[:-1])}"
               f"{',' if len(dealer_cards) > 2 else ''} and {dealer_cards[-1]}. "
               f"Dealer hand value: {get_hand_value(dealer_hand)}")
    print('')

def set_user_bet(current_cash, turn_bets, player_hand, dealer_hand):
    clear_screen()
    arrow_print('Here are the hands:\n')
    display_hands(player_hand, dealer_hand)
    total_cash = sum(current_cash)
    total_bets = sum(turn_bets)
    available_money = total_cash - total_bets

    if total_cash == total_bets:
        arrow_print(f"You've bet all your money! Press [enter] to continue.")
        input()
        return 0

    if not turn_bets:
        arrow_print("How much would you like to bet? "
        f"You've currently got ${sum(current_cash)} dollars.")
    else:
        arrow_print(f"You've already bet ${total_bets} " 
                    f"(Available: ${available_money}). " 
                    "Input a # to raise or [n] to continue.") 

    while True:
        bet = input().lstrip('$')
        if bet in ['n', 'no', 0]:
            return 0
        if is_valid_bet(bet, total_cash - total_bets):
            return int(bet)
        print("That's not a valid bet! Try again.")
        print(f"Input a positive dollar of ${available_money} or less.")

def is_valid_bet(bet, current_cash):
    return bet.isdigit() and 0 < int(bet) <= current_cash

def player_turn(deck, player_hand, dealer_hand, current_cash):
    clear_screen()
    turn_bets = []

    while True:
        if is_bust(player_hand):
            break

        display_hands(player_hand, dealer_hand)
        prompt_hint(deck, player_hand, dealer_hand)

        bet = set_user_bet(current_cash, turn_bets, player_hand, dealer_hand)
        turn_bets.append(bet)

        clear_screen()
        if get_hand_value(player_hand) == MAX_HAND:
            print("You've got 21!")
            break

        arrow_print(f"You've bet ${sum(turn_bets)} so far. Here are the hands:\n")
        display_hands(player_hand, dealer_hand)

        if prompt_player_move() == 'h':
            clear_screen()
            arrow_print("You've chosen to hit! Here is your new hand:\n")
            hit(deck, player_hand)
        else:
            clear_screen()
            arrow_print("You've chosen to stay! Dealer's move.\n")
            print('Press [enter] to continue')
            input()
            return player_hand, turn_bets

    return player_hand, turn_bets

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
    clear_screen()
    arrow_print(f'{outcome}! Here are the final hands:\n')
    display_hands(player_hand, dealer_hand, True)

def prompt_hint(deck, player_hand, dealer_hand):
    arrow_print('Need a hint? Enter [y] to simulate ' 
                'the optimal strategy and [n] to continue.')

    decision = prompt_user_decision()
    if decision == 'y':

        clear_screen()
        run_simulation(deck, player_hand, dealer_hand)

        arrow_print('To continue playing, press [enter]:')
        input()
        clear_screen()
        arrow_print('As a reminder, here are the hands:\n')
        display_hands(player_hand, dealer_hand)

def prompt_play_again(current_cash):
    if current_cash == 0:
        print(f'Current cash: ${current_cash}. Uh oh…')
        return

    arrow_print(f"Current cash: ${current_cash}. "
                "Would you like to continue playing? Enter [y/n]")

    return prompt_user_decision()

def set_cash_input():
    print('Please set your initial cash pile.')
    print('Enter a dollar amount between $1 and $500:')
    while True:
        initial_cash = input().lstrip('$')
        if is_valid_cash_pile(initial_cash):
            return int(initial_cash)
        clear_screen()
        print("That's not a valid cash amount. " 
              "Enter a positive integer between $1 and $500:")

def is_valid_cash_pile(cash):
    return cash.isdigit() and 501 > int(cash) > 0

def update_bets(outcome, turn_bets):
    match outcome.split()[0]:
        case 'Dealer':
            turn_bets = [-bet for bet in turn_bets]
        case "It's":
            turn_bets.clear()

    return turn_bets

########### Game Implementation ###########

def play_round(deck, player_hand, dealer_hand, cash):
    player_hand, turn_bets = player_turn(deck, player_hand, dealer_hand, cash)
    dealer_hand = dealer_turn(deck, dealer_hand, player_hand)
    outcome = get_outcome(player_hand, dealer_hand)

    updated_bets = update_bets(outcome, turn_bets)

    return outcome, player_hand, dealer_hand, updated_bets

def play_multiple_rounds():
    total_cash = [set_cash_input()]
    while sum(total_cash) > 0:
        clear_screen()
        deck = initialize_deck()
        arrow_print(f"You've got ${sum(total_cash)} dollars. Press [enter] to deal cards.")
        input()

        deck, player_hand, dealer_hand = deal_hands(deck)
        outcome, player_hand, dealer_hand, turn_bets = (
            play_round(deck, player_hand, dealer_hand, total_cash))

        display_winner(outcome, player_hand, dealer_hand)
        total_cash.extend(turn_bets)

        if prompt_play_again(sum(total_cash)) == 'n':
            break

    if sum(total_cash) == 0:
        print("Looks like you're all out of money!")
    else:
        clear_screen()
        arrow_print("Sorry to see you go! You're leaving with "
              f'${sum(total_cash)} dollars.\n')
    print('Press [enter] to exit the game')
    input()
    clear_screen()

def play_twenty_one():
    clear_screen()
    arrow_print('Welcome to Twenty One!\n')

    play_multiple_rounds()

    arrow_print('Thanks for playing!\n')

########### Simulation functions ###########

def set_sim_depth():
    arrow_print('How many games should I simulate?\n')
    print('Please choose an number between 1000 and 10000.')
    while True:
        sim_depth = input()
        if is_valid_sim_depth(sim_depth):
            return int(sim_depth)
        print('\nSorry, you need to input an integer ' 
              'between 1000 and 10000.')

def is_valid_sim_depth(depth):
    return depth.isdigit() and (999 < int(depth) < 10001)

def simulate_player_hand(simulated_deck, simulated_hand):

    def is_ace_in_hand(hand):
        ace_found = False
        for card_info in hand:
            for key in card_info.keys():
                if is_ace(key):
                    ace_found = True
        return ace_found

    def is_ace_fork(hand):
        return (is_ace_in_hand(hand) and 
                get_hand_value(hand) > ACE_TEST_FORK_MIN)

    hits = 0
    while not is_bust(simulated_hand):
        if is_ace_fork(simulated_hand):
            if random.choice([0, 1]):
                return simulated_hand, 0

        hit(simulated_deck, simulated_hand)
        hits += 1

    simulated_hand.pop()

    return simulated_hand, hits - 1

def play_sim_round(sim_deck, sim_player, sim_dealer):
    sim_player_hand, hits = simulate_player_hand(sim_deck, sim_player)
    sim_dealer_hand       = dealer_turn(sim_deck, sim_dealer, sim_player)
    sim_outcome           = get_outcome(sim_player_hand, sim_dealer_hand)

    return sim_outcome, hits

def randomize_hidden_card(deck, dealer_hand):
    deck_copy   = copy.deepcopy(deck)
    dealer_copy = copy.deepcopy(dealer_hand)

    hidden_card = dealer_copy.pop(0)
    deck_copy.append(hidden_card)
    sim_deck = random.sample(deck_copy, k=len(deck_copy))

    new_hidden_card = random.sample(sim_deck, k=1)[0]
    sim_deck.remove(new_hidden_card)
    sim_dealer = dealer_copy + [new_hidden_card]

    return sim_deck, sim_dealer

def run_simulation(deck, player_hand, dealer_hand):
    win_results = {}
    tie_results = {}
    current_total = get_hand_value(player_hand)

    if current_total == 21:
        clear_screen()
        print("You already have 21! You don't need a simulation.")
        return

    else:
        sim_depth = set_sim_depth()
        for _ in range(sim_depth):
            sim_deck, sim_dealer = randomize_hidden_card(deck, dealer_hand)
            sim_player           = copy.deepcopy(player_hand)
            sim_outcome, hits    = play_sim_round(sim_deck, sim_player, sim_dealer)

            if sim_outcome[0] == 'P':
                    win_results[hits] = win_results.get(hits, 0) + 1
            elif sim_outcome[0] == 'I':
                tie_results[hits] = tie_results.get(hits, 0) + 1

    win_ratios = {key: (total_wins / sim_depth)
                 for key, total_wins in win_results.items()}

    tie_ratios = {key: (total_ties / sim_depth)
                 for key, total_ties in tie_results.items()}

    ordered_results = sorted(list(win_ratios.items()), 
                             key=lambda ratios: ratios[1],
                             reverse=True)

    display_sim_results(ordered_results, tie_ratios, sim_depth)

def display_sim_results(ordered_results, tie_ratios, sim_depth):
    clear_screen()
    arrow_print(f'Simulated results for {sim_depth} games:')
    for key, win_ratio in ordered_results:
        if key == 0:
            print_string = [('Staying has   a '
                             f'{win_ratio * 100:.1f}% win rate '), 
                            (f'and a {tie_ratios[key] * 100:.1f}% '
                             'tie rate' if tie_ratios.get(key)
                            else '')]
            print(''.join(print_string))

        else:
            print_string = [(f'Hitting {key} has a '
                             f'{win_ratio * 100:.1f}% win rate '),
                            (f'and a {tie_ratios[key] * 100:.1f}% '
                             'tie rate' if tie_ratios.get(key)
                            else '')]
            print(''.join(print_string))
    print('')
    #print(f'The optimal strategy is to {get_optimal_strategy(ordered_results)}\n')

def get_optimal_strategy(ordered_results): # working but logic potentially wrong
    total_hit_win_percentage = sum([hit_num[1] * 100 for hit_num in ordered_results
                                if hit_num[0] != 0]) # is this logic right
    try:
        stay_win_percentage      = [hit_num[1] * 100 for hit_num in ordered_results 
                                   if hit_num[0] == 0][0]
    except IndexError:
        stay_win_percentage      = 0

    return 'hit' if total_hit_win_percentage > stay_win_percentage else 'stay'

play_twenty_one()