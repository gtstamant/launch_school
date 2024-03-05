def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first()) # {'prop1': 'hi there'}
print(second()) # None

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list) # [1, 2]
print(dictionary) # {'first': [1]}





def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ['one']
print(f"two is: {two}") # ['two']
print(f"three is: {three}") # ['three']




def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one
print(f"two is: {two}") # two
print(f"three is: {three}") # three


def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ['two']
print(f"two is: {two}") # ['three']
print(f"three is: {three}") # ['one']


def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separate_words) != 4:
        return False
    
    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    
    return True

if False:
    greeting = "hello world"

print(greeting)