from random import *

class Card:
    ACE_VALUE  = 11
    FACE_VALUE = 10
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        try:
            return int(self.rank)
        except ValueError:
            if self.rank == 'A':
                return self.ACE_VALUE
            return self.FACE_VALUE

    def return_ascii(self):
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

        if self.suit == 'Hearts':
            line_1 = ' _______ '
            line_2 = f'|{left_rank}_ _  |'
            line_3 = '| ( v ) |'
            line_4 = r'|  \ /  |'
            line_5 = '|   .   |'
            line_6 = f'|_____{right_rank}|'

        if self.suit == 'Diamonds':
            line_1 = ' _______ '
            line_2 = f'|{left_rank} ^   |'
            line_3 = r'|  / \  |'
            line_4 = r'|  \ /  |'
            line_5 = '|   .   |'
            line_6 = f'|_____{right_rank}|'

        if self.suit == 'Clubs':
            line_1 = ' _______ '
            line_2 = f'|{left_rank} _   |'
            line_3 = '|  ( )  |'
            line_4 = "| (_'_) |"
            line_5 = '|   |   |'
            line_6 = f'|_____{right_rank}|'

        return [line_1, line_2, line_3, line_4, line_5, line_6]

    def print_ascii(self):
        if self.rank != '10':
            left_rank = self.rank + ' '
            right_rank = ' ' + self.rank
        
        else:
            left_rank, right_rank = self.rank, self.rank

        if self.suit == 'Spades':
            print(' _______ ')
            print(f'|{left_rank} .   |')
            print(r'|  /.\  |')
            print('| (_._) |')
            print('|   |   |')
            print(f'|_____{right_rank}|')
        
        if self.suit == 'Hearts':
            print(' _______ ')
            print(f'|{left_rank}_ _  |')
            print('| ( v ) |')
            print(r'|  \ /  |')
            print('|   .   |')
            print(f'|_____{right_rank}|')

        if self.suit == 'Diamonds':
            print(' _______ ')
            print(f'|{left_rank} ^   |')
            print(r'|  / \  |')
            print(r'|  \ /  |')
            print('|   .   |')
            print(f'|_____{right_rank}|')

        if self.suit == 'Clubs':
            print(' _______ ')
            print(f'|{left_rank} _   |')
            print('|  ( )  |')
            print("| (_'_) |")
            print('|   |   |')
            print(f'|_____{right_rank}|')

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = [str(num) for num in range(2, 11)] + ['J', 'Q', 'K', 'A']
    HAND_SIZE = 2

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.SUITS
                                       for rank in self.RANKS]
        shuffle(self.cards)

    def deal(self):
        return [self.cards.pop() for _ in range(self.HAND_SIZE)]

    def hit(self):
        return [self.cards.pop()]

class Participant:
    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        self.hand = []
        self.score = 0

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        return self.get_score() > 22

    def get_score(self):
        return sum([card.get_value() for card in self.hand])
    
    def __str__(self):
        return self.__class__.__name__

class Player(Participant):
    def __init__(self):
        # STUB
        # What additional attributes might a player need?
        # Score? Hand? Amount of money available?
        pass

class Dealer(Participant):
    def __init__(self):
        # STUB
        # Very similar to a Player; do we need this?
        pass

    def hide(self):
        # STUB
        pass

    def reveal(self):
        # STUB
        pass

class TwentyOneGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        # SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        self.player.hand = self.deck.deal()
        self.dealer.hand = self.deck.deal()
    
    def show_hand(self, player):
        card_art = []
        for card in player.hand:
            card_art += [card.return_ascii()]

        print(f"{player}'s cards:")

        for line_num in range(6):
            line = ''
            for card_num in range(len(card_art)):
                line += card_art[card_num][line_num] + ' '

            print(line)

    def show_dealer_card(self):
        print("Dealer's card:")
        self.dealer.hand[0].print_ascii()

    def show_cards(self):
        self.show_hand(self.player)
        print()
        self.show_dealer_card()

    def show_cards_w_dealer(self):
        self.show_hand(self.player)
        print()
        self.show_hand(self.dealer)
    
    def player_turn(self):
        while not self.player.is_busted():
            print('Would you like to hit or stay?: ')
            
            while True:
                choice = input().lower()
                if choice in ['hit', 'stay']:
                    break

                print("That's not a valid input. Please type 'hit' or 'stay'.")
            
            if choice == 'stay':
                print("You have chosen to stay. Dealer's turn.")
                break
            
            self.player.hand += self.deck.hit()

            print('Here are the hands:')
            self.show_cards()

    def dealer_turn(self):
        
        while self.dealer.get_score() < 17 and not self.player.is_busted():
            self.dealer.hand += self.deck.hit()
            print('Dealer draws:')
            self.dealer.hand[-1].print_ascii()
            
            if self.dealer.is_busted():
                print('Dealer is bust!')
                break
                
        print("Here are the final hands: ")
        self.show_cards_w_dealer()

    def display_welcome_message(self):
        print('Welcome to 21!')

    def display_goodbye_message(self):
        print('Thanks for playing!')

    def display_result(self):
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
            
        print(f'{winner} wins with a score of {winner.get_score()}')
        print(f'{loser} loses with a score of {loser.get_score()}')

game = TwentyOneGame()
game.start()