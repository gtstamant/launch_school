import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER  = " "
    HUMAN_MARKER    = "X"
    COMPUTER_MARKER = "O"
    
    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker
    
    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker
    
    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER
    
    def __str__(self):
        return self.marker

class Board:
    def __init__(self):
        self.squares = {num: Square() for num in range(1, 10)}

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker
   
    def is_unused_square(self, key):
        return self.squares[key].is_unused()
    
    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]
    
    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |" 
              f"  {self.squares[5]}  |" 
              f"  {self.squares[6]}")
        print("     |     | ")
        print("-----+-----+-----")
        print("     |     | ")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |" 
              f"  {self.squares[9]}")
        print("     |     | ")
        print()

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

class Player:
    def __init__(self, marker):
        self.marker = marker
        self._score = 0

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value

    def increment_score(self):
        self.score += 1
    
    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    MATCH_GOAL = 3
    
    @staticmethod
    def _join_or(lst, sep=',', conj='or'):
        sep += ' '

        if len(lst) < 2:
            return f'{lst[0]}'
        if len(lst) == 2:
            return f'{lst[0]}{sep}{lst[1]}'
    
        return (f'{sep.join([str(item) for item in lst[:-1]])}{sep}'
                f'{conj} {lst[-1]}')

    def __init__(self):
        self.human = Human()
        self.computer = Computer()

    def play(self):
        self.board = Board()

        while True:
            self.board.display()
            self.human_moves()
            
            if self.is_game_over():
                break
            
            self.computer_moves()
            if self.is_game_over():
                break

            self.board.display_with_clear()

        self.board.display_with_clear()
        self.display_results()
    
    def play_ttt(self):
        
        self.display_welcome_message()
        self.play_match()
        self.display_goodbye_message()

    def play_again(self):
        while True:
            answer = input("Play again (y/n)? ").lower()

            if answer in ["y", "n"]:
                break

            print("Sorry, that's not a valid choice.\n")

        clear_screen()
        return answer == "y"

    def play_match(self):
        print(f'The first player to win {TTTGame.MATCH_GOAL} '
              f'games wins the match.')
        
        while True:
            self.play()
            self.update_match_score()
            self.display_match_score()

            if self.match_over():
                break
            if not self.play_again():
                break
        
        self.display_match_results()
    
    def match_over(self):
        return (self.is_match_winner(self.human) or
                self.is_match_winner(self.computer))
    
    def is_match_winner(self, player):
        return player.score >= TTTGame.MATCH_GOAL
    
    def update_match_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()
        elif self.is_winner(self.computer):
            self.computer.increment_score()
    
    def display_match_score(self):
        human = self.human.score
        computer = self.computer.score
        print('Current match score: '
              f"[you: {human}] [computer: {computer}]")
    
    def display_match_results(self):
        if self.human.score > self.computer.score:
            print('You won this match! Congratulations.')
        else:
            print('Oh, boo hoo. You lost the match.')
    
    def display_welcome_message(self):
        clear_screen()
        print('Welcome to Tic Tac Toe!')
        print()

    def display_goodbye_message(self):
        print('Thanks for playing Tic Tac Toe! '
              'Goodbye!')

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def human_moves(self):
        choice = None
        while True:
            valid_choices = self.board.unused_squares()
            printable_choices = TTTGame._join_or(valid_choices)
            prompt = f'Choose a square ({printable_choices}) '
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass
            
            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, Square.HUMAN_MARKER)

    def computer_moves(self):
        MIDDLE_SQUARE = 5

        for player in (self.computer, self.human):
            choice = self.ai_computer_move(player)

            if choice:
                self.board.mark_square_at(choice, self.computer.marker)

        if not choice:
            valid_choices = self.board.unused_squares()
            if MIDDLE_SQUARE in valid_choices:
                choice = MIDDLE_SQUARE
            else:
                choice = random.choice(valid_choices)
        
        self.board.mark_square_at(choice, self.computer.marker)

    def ai_computer_move(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            attack = self.at_risk_square(player, row)
            if attack:
                return attack
        
        return None
    
    def at_risk_square(self, player, row):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key
        
        return None

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

game = TTTGame()
game.play_ttt()