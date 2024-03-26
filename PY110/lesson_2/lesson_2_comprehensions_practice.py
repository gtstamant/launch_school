# Problem 1

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total = 0
for data in munsters.values():
    if data['gender'] == 'male':
        total += data['age']

age = [data['age'] for data in munsters.values()
       if data['gender'] == 'male']

# print(sum(age))

# Problem 2

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_list = []
for sublist in lst:
    new_list.append(sorted(sublist))

# print(new_list)
    
new_lst = [sorted(sublist) for sublist in lst]

# Problem 3

new_lst = [sorted(sublist, key=str) for sublist in lst]
# print(new_lst)

# Problem 4

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dictionary = {sublist[0]: sublist[1] 
              for sublist in lst}

# Problem 5

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def add_odds(lst):
    return sum([num for num in lst
                if num % 2 != 0])

new_lst = sorted(lst, key=add_odds)

# Problem 6

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_lst = [
    {key: value + 1 for key, value in subdict.items()} 
    for subdict in lst
]

def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

new_lst = [increment_values(dictionary) for dictionary in lst]

# Problem 7

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [
    [num for num in sublist if num % 3 == 0]
    for sublist in lst
]

def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

new_lst = [divisible_by_3(sublist) for sublist in lst]

# Problem 8

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def get_datum(dictionary):
    match dictionary.get('type'):
        case 'fruit'    : return [color.capitalize() 
                          for color in dictionary.get('colors')]
        case 'vegetable': return dictionary.get('size').upper()

data_lst = [get_datum(value) for value in dict1.values()]

# Problem 9

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def check_values(dictionary):
    for value in dictionary.values():
        for element in range(len(value)):
            if value[element] % 2 != 0:
                return False
    return True

def all_even(dictionary):
    for value in dictionary.values():
        if any([num % 2 for num in value]):
            return False
    return True

def list_even(lst):
    return not any([num % 2 for num in lst])

def all_even(dictionary):
    return (all([list_even(list_value) 
                     for list_value in dictionary.values()]))

new_lst = [subdict for subdict in lst 
                   if all_even(subdict)]

# Problem 10

import random

# def generate_uuid():
#     num_range = [num for num in range(10)]
#     num_range += ['a', 'b', 'c', 'd', 'e', 'f']

#     uuid_nums = [str(element) for element
#                 in random.choices(num_range, k=32)]
    
#     uuid = (''.join(uuid_nums[:9])    + '-' +
#             ''.join(uuid_nums[9:13])  + '-' +
#             ''.join(uuid_nums[13:17]) + '-' +
#             ''.join(uuid_nums[17:21]) + '-' +
#             ''.join(uuid_nums[21:])
#             )
            

#     return uuid

def generate_uuid():
    hex_chars = '0123456789abcdef'
    divisions = [8, 4, 4, 4, 12]
    uuid = []

    for division in divisions:
        chars = [random.choice(hex_chars) for _ in range(division)]
        uuid.append(''.join(chars))
    
    return '-'.join(uuid)

# Problem 11

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = 'aeiou'
vowel_lst = []

for list in dict1.values():
    for element in list:
        for char in element:
            if char in vowels:
                vowel_lst.append(char)

vowel_lst = [char for list in dict1.values()
             for element in list
             for char in element
             if char in vowels]

print(vowel_lst)