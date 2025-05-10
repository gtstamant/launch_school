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

class DisplayMixin:
    def display_cards(self, player, dealer):
        print('Here are the hands:')
        print()
        player.hand.render_hand(self.player)
        print()
        dealer.hand.render_hand(self.dealer)
        print()

    def display_player_score(self, player):
        print(f'|| Player score: {player.hand.get_score()} '
              f'|| Player cash: ${player.get_money()} ||')
        print()

    def display_result(self, player, dealer):
        if not self.is_tied(player, dealer):
            winner, loser = self.get_winner_and_loser(player, dealer)

            print(f'|| {winner.get_role()} wins. '
                  f'Score: {winner.hand.get_score()} '
                  f'|| {loser.get_role()} loses. '
                  f'Score: {loser.hand.get_score()} ||')
            print()
        else:
            print(f'|| {self.player} ties. '
                  f'Score: {self.player.hand.get_score()} || '
                  f'{self.dealer} ties. '
                  f'Score: {self.dealer.hand.get_score()} ||')
            print()

    def display_goodbye_message(self):
        if self.player.is_rich():
            print("You're too rich. No more money for you!")
        elif self.player.is_out_of_money():
            print("Uh oh...you're out of cash!")
        else:
            clear_screen()
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

    def hide(self):
        self.hidden = True

    def reveal(self):
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

class Hand(DisplayMixin):
    def __init__(self):
        self.cards = []

    def add_card(self, new_card, face_down=False):
        if face_down:
            new_card.hide()
        
        self.cards.append(new_card) 

    def reset_hand(self):
        self.cards.clear()

    def render_hand(self, player):
        card_art = []
        for card in self.cards:
            card_art += [card.get_card_ascii()]

        print(f"{player}'s cards:" if not player.is_busted()
                                   else f"{player} busts!")

        for line_num in range(6):
            line = ''
            for card_num in range(len(card_art)):
                line += card_art[card_num][line_num] + ' '

            print(line)

    def get_score(self):
        total = sum([card.get_value() for card in self.cards])
        ranks = [card.rank for card in self.cards]

        if total > 21 and 'A' in ranks:
            num_aces = ranks.count('A')

            while num_aces > 0 and total > 21:
                total -= 10
                num_aces -= 1

        return total

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS
                                       for rank in Card.RANKS]
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Participant(DisplayMixin):
    VALID_CHOICES = ['h', 's']
    TARGET_CASH = 10

    def __init__(self, role, money=0):
        self.hand = Hand()
        self.role = role
        self.money = money

    def get_money(self):
        return self.money

    def get_role(self):
        return self.role

    def is_out_of_money(self):
        return self.money == 0

    def is_rich(self):
        return self.money >= self.TARGET_CASH

    def is_busted(self):
        return self.hand.get_score() > 21
    
    def __str__(self):
        return self.role

class TwentyOneGame(DisplayMixin):
    ACE_VALUE  = 11
    FACE_VALUE = 10
    HAND_SIZE = 2
    WINNING_SCORE = 21
    DEALER_MAX = 17
    BET_SIZE = 1
    STAY = 's'
    HIT = 'h'

    def __init__(self, player, dealer):
        self.deck = Deck()
        self.player = player
        self.dealer = dealer
    
    def deal_hands(self):
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card(), face_down=True)

    def play_turn(self, player):
        match player.get_role():
            case 'Player': self._player_turn()
            case 'Dealer': self._dealer_turn()
    
    def _player_turn(self):
        while self.player.hand.get_score() < self.WINNING_SCORE:
            self.display_player_score(self.player)
            choice = prompt_valid_input(Participant.VALID_CHOICES)

            if choice == self.STAY:
                break

            self.player.hand.add_card(self.deck.deal_card())

            clear_screen()
            self.display_cards(self.player, self.dealer)

    def _dealer_turn(self):
        self.dealer.hand.cards[1].reveal()
        while (self.dealer.hand.get_score() < self.DEALER_MAX and
               not self.player.is_busted()):
            clear_screen()
            self.dealer.hand.add_card(self.deck.deal_card())

            if self.dealer.hand.get_score() >= self.DEALER_MAX:
                break

            self.display_cards(self.player, self.dealer)
            input(f'|| Dealer score: {self.dealer.hand.get_score()} '
                   '|| Press [enter] to continue...')

        clear_screen()
        self.display_cards(self.player, self.dealer)

    def is_tied(self, player, dealer):
        return player.hand.get_score() == dealer.hand.get_score()

    def get_winner_and_loser(self, player, dealer):
        player_score = player.hand.get_score()
        dealer_score = dealer.hand.get_score()

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

    def adjust_money(self, bet, player, dealer):
        if not self.is_tied(player, dealer):
            winner = self.get_winner_and_loser(player, dealer)[0]

            if winner is self.player:
                self.player.money += bet
            else:
                self.player.money -= bet

    def start_game(self):
        self.deal_hands()
        self.display_cards(self.player, self.dealer)
        self.play_turn(self.player)
        self.play_turn(self.dealer)
        self.display_result(self.player, self.dealer)
        self.adjust_money(self.BET_SIZE, self.player, self.dealer)

class TwentyOneSeries(DisplayMixin):
    PLAY_AGAIN_CHOICES = ['y', 'n']

    def __init__(self):
        self.player = Participant('Player', 5)
        self.dealer = Participant('Dealer')

    def play_again(self):
        play_again_message = (f'You still have ${self.player.money}! '
                              'Play again? ')
        user_choice = prompt_valid_input(self.PLAY_AGAIN_CHOICES,
                                      play_again_message)

        return user_choice == 'y'

    def start_series(self):
        while True:
            game = TwentyOneGame(self.player, self.dealer)
            self.player.hand.reset_hand()
            self.dealer.hand.reset_hand()
            game.start_game()

            if ((self.player.is_out_of_money() or
                self.player.is_rich()) or
                not self.play_again()):
                break

            clear_screen()

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