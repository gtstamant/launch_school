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
OUTLIER_PRUNING_LIMIT = 20

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

    def is_high_ace_in_hand(hand):
        high_ace_found = False
        for card_info in hand:
            for key, value in card_info.items():
                if is_ace(key) and value == HIGH_ACE_VALUE:
                    high_ace_found = True
        return high_ace_found

    def is_ace_fork(hand):
        return (is_high_ace_in_hand(hand) and 
                get_hand_value(hand) > ACE_TEST_FORK_MIN)

    def restore_original_hand(new_hand, original_hand):
        new_hand_cards = [key for card_info in new_hand
                          for key in card_info.keys()]
        old_hand_cards = [key for card_info in original_hand
                          for key in card_info.keys()]
        
        if new_hand_cards == old_hand_cards:
            return original_hand
        
        return new_hand

    hits = 0
    busts = 0
    original_hand = copy.deepcopy(simulated_hand)
    while not is_bust(simulated_hand):
        if is_ace_fork(simulated_hand):
            if random.choice([0, 1]):
                # hit(simulated_deck, simulated_hand)
                # if is_bust(simulated_hand):
                    # busts += 1
                # print(f'Orig hand: {original_hand}')
                # input()
                return simulated_hand, hits, busts

        hit(simulated_deck, simulated_hand)
        hits += 1
        if is_bust(simulated_hand):
            busts += 1

    simulated_hand.pop()
    simulated_hand = restore_original_hand(simulated_hand, original_hand)

    return simulated_hand, hits - 1, busts

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

def play_sim_round(sim_deck, sim_player, sim_dealer):
    sim_player_hand, hits, busts = simulate_player_hand(sim_deck, sim_player)
    # if hits == 0:
    #     print(sim_player_hand)
    #     input()
    
    sim_dealer_hand       = dealer_turn(sim_deck, sim_dealer, sim_player)
    sim_outcome           = get_outcome(sim_player_hand, sim_dealer_hand)

    return sim_outcome, hits, busts

def run_simulation(deck, player_hand, dealer_hand):
    
    def get_percent_chance_no_bust(simulation_results):
        ordered_keys = sorted(list(simulation_results.keys()))
        
        hits_past = {num: simulation_results[num][3] for num in ordered_keys}
        
        hits_at_level = {}
        running_total = 0

        for num in hits_past:
            running_total += hits_past[num]
            hits_at_level[num] = running_total

        # % chance of reaching a level without busting
        level_total = {num: sum(simulation_results[num][:-1]) 
                           for num in ordered_keys}
        # sum(data[:-1]) for data in simulation_results.values()]

        aggregate_level = {num: level_total[num] + hits_at_level[num - 1]
                          for num in ordered_keys[1:]}
        
        chance_to_level = {num: (level_total[num]/aggregate_level[num])
                        for num in aggregate_level.keys()}
        chance_to_level[ordered_keys[0]] = 1 # 100% chance of reaching level

        return chance_to_level

    def get_ratios(simulation_results):
        
        def get_ratio(dictionary, key, win_or_tie):
            # win = 0, tie = 1; fix later
            try:
                return (dictionary[key][win_or_tie] /
                        sum(dictionary[key][:-1]))
            except ZeroDivisionError:
                return 0
        
        ordered_keys = sorted(list(simulation_results.keys()))
        
        percentage_to_hit_level = get_percent_chance_no_bust(simulation_results)
        
        local_win_ratios = {num: get_ratio(simulation_results, num, 0)
                            for num in ordered_keys}
        local_tie_ratios = {num: get_ratio(simulation_results, num, 1)
                            for num in ordered_keys}
        
        global_win_ratios = {num: (local_win_ratios[num] *
                          percentage_to_hit_level[num])
                          for num in ordered_keys}
        
        global_tie_ratios = {num: (local_tie_ratios[num] *
                          percentage_to_hit_level[num])
                          for num in ordered_keys}
    
        return global_win_ratios, global_tie_ratios    
    
    simulation_results = {}
    current_total = get_hand_value(player_hand)

    if current_total == 21:
        clear_screen()
        print("You already have 21! You don't need a simulation.")
        return None
    else:
        sim_depth = set_sim_depth()
        for _ in range(sim_depth):
            sim_deck, sim_dealer = randomize_hidden_card(deck, dealer_hand)
            sim_player           = copy.deepcopy(player_hand)
            sim_outcome, hits, busts = play_sim_round(sim_deck, sim_player, sim_dealer)

            if hits not in simulation_results:
                simulation_results[hits] = [0, 0, 0, 0]
            elif sim_outcome[0] == 'P':
                simulation_results[hits][0] += 1
            elif sim_outcome[0] == 'I':
                simulation_results[hits][1] += 1
            else:
                simulation_results[hits][2] += 1
            
            simulation_results[hits][3] += busts

    win_ratios, tie_ratios = get_ratios(simulation_results)
    
    ordered_keys = sorted(list(win_ratios.keys()))
    for num in ordered_keys: # rewrite
        if num == 0:
            print(f'Stay: win rate {win_ratios[num] * 100:.2f}%, tie: {tie_ratios[num] * 100:.2f}%')
        else:
            print(f'{num}: win rate {win_ratios[num] * 100:.2f}%, tie: {tie_ratios[num] * 100:.2f}%')

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
    #print('The optimal strategy is to ' 
    # f'{get_optimal_strategy(ordered_results)}\n')

## Removed the following function as 
## I am not certain whether the logic is quite right

# def get_optimal_strategy(ordered_results):
#     total_hit_win_percentage = sum([hit_num[1] * 100 for hit_num in ordered_results
#                                 if hit_num[0] != 0]) # is this logic right
#     try:
#         stay_win_percentage      = [hit_num[1] * 100 for hit_num in ordered_results
#                                    if hit_num[0] == 0][0]
#     except IndexError:
#         stay_win_percentage      = 0

#     return 'hit' if total_hit_win_percentage > stay_win_percentage else 'stay'

play_twenty_one()