# 1

fruits = ("apple", "banana", "cherry", "date", "banana")
print(fruits.count('banana'))

# 2

# We would expect the code to print 5

# 3

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a | b # union, does not mutate; eq. a.union(b)

print(c)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a |= b # Known as 'update', mutates a
print(a)

# 4
"""
We would expect (pp for clarity): 

{
    'Fred': 0, 
    'Barney': 1, 
    'Wilma': 2, 
    'Betty': 3,
    'Pebbles': 4,
    'Bambam': 5,
}

"""
# 5

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_age = 0

for age in ages.values():
    total_age += age

print(total_age)

# More idiomatic solution:

total_age = sum(ages.values())
print(total_age)

# 6

min_age = min(ages.values())

print(min_age)

# 7

# ['bear']

# 8
from pprint import pp

statement = "The Flintstones Rock"

# char_freq = {}

# for char in statement.replace(' ', ''):
#     if char not in char_freq:
#         char_freq[char] = 1
#     else:
#         char_freq[char] += 1

# pp(char_freq)

# Less verbose solution

char_freq = {}
statement = statement.replace(' ', '')

for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

#pp(char_freq)
   
# 9

# [2, 3]
    
# 10

# ('b': 'bear'), returns last item added to dict as tuple key, value pair
# Recent implementations of python maintain order in which items were added to dict
# So we know that 'b', 'bear' was the last item
    
# 11

# [1, 2]
    
# 12

# AttributeError, no add attribute for frozenset