"""
Mutability and immutability
- variables as pointers
- shallow and deep copies
"""

lst_1 = [num for num in range(5)]
# print(lst_1)

lst_2 = lst_1
lst_1[2] = 'New value!'
# print(lst_2)

#######

lst_1 = [[num, num * 2] for num in range(5)]
#print(lst_1)
tup_1 = tuple(lst_1)

tup_1[1][1] = 'New val'
# print(tup_1)
 
#######

dict_1 = {str(num): num for num in range(5)}
# print(dict_1)

dict_2 = dict(dict_1)
dict_2['1'] = 'one'

# print(dict_1)

dict_1 = {str(num): [num, num * 2] for num in range(5)}
# print(dict_1)

dict_2 = dict_1
dict_2['0'][1] = 'new value'

# print(dict_1)

#######

"""
Variable scope
- variable shadowing
"""

number = 10
number_2 = 15

def add_numbers(number, number_2):
    number = 15

    return number + number_2

print(add_numbers(number, number_2))

#######

my_list = ['a', 'b', ['c', 'd']]

def mutate_list(lst):
    while True:
        break

    my_lst = ['a', 'b', ['c', 'd']]

    for idx in range(len(lst)):
        my_lst[idx] = idx

    return my_lst
    
print(mutate_list(my_list))
print(my_list)


"""
Functions
- Output, return values, side effects

"""

"""

"""