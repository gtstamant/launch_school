from pprint import pprint as pp

NAMES = [
    'zero', 
    'one', 
    'two', 
    'three', 
    'four', 
    'five', 
    'six', 
    'seven', 
    'eight', 
    'nine', 
    'ten', 
    'eleven', 
    'twelve', 
    'thirteen', 
    'fourteen', 
    'fifteen', 
    'sixteen', 
    'seventeen', 
    'eighteen', 
    'nineteen',
]

NAMES = {num: NAMES[num] for num in range(0, 20)}

def get_name(num):
    return NAMES[num]

def alphabetic_number_sort(num_lst):
    return sorted(num_lst, key=get_name)

pp(alphabetic_number_sort(
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
# [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
