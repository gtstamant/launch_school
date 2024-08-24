import os
from random import shuffle

def clear_screen():
    os.system('clear')

def prompt_valid_input(valid_inputs, message=''):
    print(f'{message}Please choose: {valid_inputs}: ')

    while True:
        choice = input().lower()
        if choice in valid_inputs:
            break
 
        print(f"That's not a valid input. Please choose from {valid_inputs}.")

    return choice

class Card:
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = [str(num) for num in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hidden = False

    def get_value(self):
        try:
            return int(self.rank)

        except ValueError:
            if self.rank == 'A':
                return TwentyOneGame.ACE_VALUE

            return TwentyOneGame.FACE_VALUE

    def hide_card(self):
        self.hidden = True
    
    def reveal_card(self):
        self.hidden = False
    
    def is_hidden(self):
        return self.hidden
    
    def get_card_ascii(self):
        if self.is_hidden():
            line_1 = ' _______ '
            line_2 = '|_______| '
            line_3 = '|_______|'
            line_4 = '|_______|'
            line_5 = '|_______|'
            line_6 = '|_______| '
            
            return [line_1, line_2, line_3, line_4, line_5, line_6]

        if self.rank != '10':
            left_rank = self.rank + ' '
            right_rank = ' ' + self.rank

        else:
            left_rank, right_rank = self.rank, self.rank

        if self.suit == 'Spades':
            line_1 = ' _______ '
            line_2 = f'|{left_rank} .   |'
            line_3 = r'|  /.\  |'
            line_4 = '| (_._) |'
            line_5 = '|   |   |'
            line_6 = f'|_____{right_rank}|'

        elif self.suit == 'Hearts':
            line_1 = ' _______ '
            line_2 = f'|{left_rank}_ _  |'
            line_3 = '| ( v ) |'
            line_4 = r'|  \ /  |'
            line_5 = '|   .   |'
            line_6 = f'|_____{right_rank}|'

        elif self.suit == 'Diamonds':
            line_1 = ' _______ '
            line_2 = f'|{left_rank} ^   |'
            line_3 = r'|  / \  |'
            line_4 = r'|  \ /  |'
            line_5 = '|   .   |'
            line_6 = f'|_____{right_rank}|'

        elif self.suit == 'Clubs':
            line_1 = ' _______ '
            line_2 = f'|{left_rank} _   |'
            line_3 = '|  ( )  |'
            line_4 = "| (_'_) |"
            line_5 = '|   |   |'
            line_6 = f'|_____{right_rank}|'

        return [line_1, line_2, line_3, line_4, line_5, line_6]

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS
                                       for rank in Card.RANKS]
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.cards)
    
    def deal_cards(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

class Participant:
    VALID_CHOICES = ['h', 's']

    def __init__(self, role, money=0):
        self.hand = []
        self.role = role
        self.money = money
        self.TARGET_CASH = 10

    def get_money(self):
        return self.money

    def get_role(self):
        return self.role

    def is_out_of_money(self):
        return self.money == 0

    def is_rich(self):
        return self.money > self.TARGET_CASH

    def is_busted(self):
        return self.get_score() > 21

    def get_score(self):
        total = sum([card.get_value() for card in self.hand])
        ranks = [card.rank for card in self.hand]

        if total > 21 and 'A' in ranks:
            num_aces = ranks.count('A')

            while num_aces > 0 and total > 21:
                total -= 10
                num_aces -= 1

        return total

    def __str__(self):
        return self.role

class TwentyOneGame:
    ACE_VALUE  = 11
    FACE_VALUE = 10
    HAND_SIZE = 2
    WINNING_SCORE = 21
    DEALER_MAX = 17
    DEALER_HIDDEN_CARD_IDX = 1
    STAY = 's'
    HIT = 'h'

    def __init__(self, player, dealer):
        self.deck = Deck()
        self.player = player
        self.dealer = dealer

    def deal_hands(self):
        self.player.hand = self.deck.deal_cards(TwentyOneGame.HAND_SIZE)
        self.dealer.hand = self.deck.deal_cards(TwentyOneGame.HAND_SIZE)
        self.dealer.hand[self.DEALER_HIDDEN_CARD_IDX].hide_card()

    def show_hand(self, player):
        card_art = []
        for card in player.hand:
            card_art += [card.get_card_ascii()]

        print(f"{player}'s cards:" if not player.is_busted() 
                                   else f"{player} busts!")

        for line_num in range(6):
            line = ''
            for card_num in range(len(card_art)):
                line += card_art[card_num][line_num] + ' '

            print(line)

    def show_cards(self):
        print('Here are the hands:')
        print()
        self.show_hand(self.player)
        print()
        self.show_hand(self.dealer)
        print()
    
    def display_player_score(self):
        print(f'|| Player score: {self.player.get_score()} '
              f'|| Player cash: ${self.player.get_money()} ||')
        print()

    def display_result(self):
        if not self.is_tied():
            winner, loser = self.get_winner_and_loser()

            print(f'|| {winner.get_role()} wins. Score: {winner.get_score()} '
                  f'|| {loser.get_role()} loses. Score: {loser.get_score()} ||')
            print()
        else:
            print(f'|| {self.player} ties. Score: {self.player.get_score()} || '
                  f'{self.dealer} ties. Score: {self.dealer.get_score()} ||')
            print()
    
    def player_turn(self):
        while self.player.get_score() < self.WINNING_SCORE:
            self.display_player_score()
            choice = prompt_valid_input(Participant.VALID_CHOICES)

            if choice == self.STAY:
                break

            self.player.hand += self.deck.deal_cards(1)

            clear_screen()
            self.show_cards()

    def dealer_turn(self):
        self.dealer.hand[1].reveal_card()
        while self.dealer.get_score() < self.DEALER_MAX and not self.player.is_busted():
            clear_screen()
            self.dealer.hand += self.deck.deal_cards(1)

            if self.dealer.get_score() >= self.DEALER_MAX:
                break

            self.show_cards()
            input(f'|| Dealer score: {self.dealer.get_score()} || Press [enter] to continue...')

        clear_screen()
        self.show_cards()

    def is_tied(self):
        return self.player.get_score() == self.dealer.get_score()
    
    def get_winner_and_loser(self):
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()

        if self.player.is_busted():
            winner = self.dealer
            loser = self.player
        elif self.dealer.is_busted():
            winner = self.player
            loser = self.dealer
        elif player_score > dealer_score:
            winner = self.player
            loser = self.dealer
        else:
            winner = self.dealer
            loser = self.player

        return winner, loser
    
    def adjust_money(self):
        if not self.is_tied():
            winner, loser = self.get_winner_and_loser()

            if winner is self.player:
                self.player.money += 1
            else:
                self.player.money -= 1

    def start_game(self):
        self.deal_hands()
        self.show_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.adjust_money()

class TwentyOneSeries():
    PLAY_AGAIN_CHOICES = ['y', 'n']

    def __init__(self):
        self.player = Participant('Player', 5)
        self.dealer = Participant('Dealer')
    
    def play_again(self):
        play_again_message = f'You still have ${self.player.money}! Play again? '
        user_choice = prompt_valid_input(self.PLAY_AGAIN_CHOICES, 
                                      play_again_message)

        return False if user_choice == 'n' else True

    def start_series(self):
        while True:
            game = TwentyOneGame(self.player, self.dealer)
            game.start_game()

            if ((self.player.is_out_of_money() or 
                self.player.is_rich()) or
                not self.play_again()):
                break

            clear_screen()

    def display_goodbye_message(self):
        clear_screen()
        if self.player.is_rich():
            print("You're too rich, time to end the game!")
        elif self.player.is_out_of_money():
            print("Uh oh...you're out of cash!")
        else:
            print(f'Player ends with ${self.player.money}')

        print()
        print('Game over. Thanks for playing!')
        print()
        print('Press [enter] to exit the game')
        input()
        clear_screen()

    def display_welcome_message(self):  
        clear_screen()
        print(f'Welcome to 21! Player starts with ${self.player.money}')
        print()
    
    def prompt_confirmation(self):
        print('Press [enter] to start the series')
        input()
        clear_screen()

    def play_series(self):
        self.display_welcome_message()
        self.prompt_confirmation()
        self.start_series()
        self.display_goodbye_message()

series = TwentyOneSeries()
series.play_series()