"""
Mutability and immutability
- variables as pointers
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
print(dict_1)
dict_2 = dict(dict_1)
dict_2['1'] = 'one'
print(dict_1)

"""
Variable scope
- variable shadowing
"""

"""
Functions
- Output, return values, side effects

"""

"""

"""