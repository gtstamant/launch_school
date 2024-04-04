"""
Mutability and immutability
- variables as pointers
- shallow and deep copies
"""
############################################

# Point: variable aliasing, variables as pointers

lst_1 = [num for num in range(5)]

# print(lst_1)

lst_2 = lst_1
lst_1[2] = 'New value!'
# print(lst_2)

############################################

# Point: mutability?, shallow copying, variables as pointers & nestd objects

lst_1 = [[num, num * 2] for num in range(5)]

#print(lst_1)
tup_1 = tuple(lst_1) # note immutable data type, shallow copy with constructor function

tup_1[1][1] = 'New val'
# print(tup_1)
 
############################################

# Point: more on copies

dict_1 = {str(num): num for num in range(5)}
# print(dict_1)

dict_2 = dict(dict_1) # copy with constructor function
dict_2['1'] = 'one'

# print(dict_1)

dict_1 = {str(num): [num, num * 2] for num in range(5)}
# print(dict_1)

dict_2 = dict(dict_1) # only a shallow copy, how might we fix?
dict_2['0'][1] = 'new value'

# print(dict_1)

############################################

"""
Variable scope
- variable shadowing
"""

############################################

# Point: variable shadowing

number = 10
number_2 = 15

def add_numbers(number, number_2):
    number = 15

    return number + number_2

# print(add_numbers(number, number_2))

############################################

# Point: More variable shadowing, returning a value vs. mutation

my_list = ['a', 'b', ['c', 'd']]

def mutate_list(lst):
    while True:
        break

    my_lst = ['a', 'b', ['c', 'd']]

    for idx in range(len(lst)):
        my_lst[idx] = idx

    return my_lst
    
# print(mutate_list(my_list))
# print(my_list)

############################################

# Point: Nested functions & variable scope

squares = {num: num ** 2 for num in range(5)}

def modify_dictionary(my_dict):

    def make_modifications(my_dict):

        # my_dict = {'a': 1} # Next try commenting this out

        def make_more_modifications(my_dict):
            
            my_dict['a'] = 2
            print(f'At "make more" ==> {my_dict}')
    
        make_more_modifications(my_dict)
        
        print(f'At "make mod" ==> {my_dict}')
    
    make_modifications(squares)

    print(f'At "mod dict" ==> {my_dict}')

# print(f'Outside ==> {modify_dictionary(squares)}')
# print(squares)
# reassign

############################################

# Point: Immutability, what actually is a function doing?

a_string = 'Here is a string!'

def string_shift(my_string):
    for char in my_string:
        char += '1'
    
    return my_string

# print(string_shift(a_string))

############################################

# Point: Why is this still wrong? What actually is a function doing?

a_string = 'Here is a string!'

def string_shift_2(my_string):
    my_list = list(my_string)
    for char in my_list:
        char += '1'

    return ''.join(my_list)

# print(string_shift_2(a_string))

############################################

# Why is this different from the above?

a_string = 'Here is a string!'

def string_shift_3(my_string):
    my_list = list(my_string)
    
    for idx in range(len(my_string)):
        my_list[idx] += '1'
    
    return ''.join(my_list)

print(string_shift_3(a_string))


"""
Functions
- Output, return values, side effects

"""

# Point: Print vs. return value

def do_something(some_argument): # What do we call the variable in the parentheses?
    print(some_argument)

# print(do_something("Here's an argument!"))

############################################

# Talk me through the following function at both an implementation level
# and user level

from pprint import pprint

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
FACE_VALUES = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

def create_deck_of_cards(card_suits, face_card_values):
    
    def generate_rank_list():
        non_face_cards = []
        face_cards = []

        for number in range(2, 11):
            non_face_cards.append(number)
        
        for face_card in face_card_values:
            face_cards.append(face_card)
        
        return non_face_cards + face_cards
    
    def initialize_deck(rank_list):
        deck = []

        for suit in card_suits:
            for rank in rank_list:
                if isinstance(rank, int):
                    deck.append({f'{rank} of {suit}': rank})
                else:
                    deck.append({f'{rank} of {suit}': face_card_values[rank]})
        
        return deck
    
    rank_list = generate_rank_list()
    deck = initialize_deck(rank_list)

    return deck

# pprint(create_deck_of_cards(SUITS, FACE_VALUES))

# Method vs. function; concatenate vs. merge?; array?

############################################

# Optimizing with comprehensions, may be too hard

def create_deck_of_cards_2(card_suits, face_card_values):
    
    def generate_rank_list():
        non_face_cards = [number for number in range(2, 11)]
        face_cards = [face_card for face_card in face_card_values]

        return non_face_cards + face_cards
    
    def initialize_deck(rank_list):
        deck = [{f'{rank} of {suit}': rank} if isinstance(rank, int)
                 else {f'{rank} of {suit}': face_card_values[rank]}
                 for suit in card_suits
                 for rank in rank_list]

        return deck
    
    rank_list = generate_rank_list()
    deck = initialize_deck(rank_list)

    return deck

# pprint(create_deck_of_cards_2(SUITS, FACE_VALUES))