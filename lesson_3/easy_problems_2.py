numbers = [1, 2, 3, 4, 5]
numbers.reverse()

print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers = numbers[::-1]
print(numbers)

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False
number2 = 95 # True

print(number1 in numbers)
print(number2 in numbers)

for num in range(10, 101):
    if num == 42:
        outcome = 'True'
    else:
        outcome = 'False'
print(outcome)

a_list = [1, 2, 3, 4, 5]
a_list.pop(2)
print(a_list)

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(isinstance(numbers, list))
print(isinstance(table, list))

title = "Flintstone Family Members"
centered_title = title.center(40)
print(centered_title)

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'), statement2.count('t'))

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages)

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

for name, age in additional_ages.items():
    ages[name] = age

print(ages)

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
print(ages)