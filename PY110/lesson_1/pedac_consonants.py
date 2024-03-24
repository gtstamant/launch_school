# 1.  Start with a list of strings as input

# 2. Consider each word in the string
#     - determine how many adjacent consonants (sub-process)
#     - store string name and number of adjacent consonants in 'results' data structure

# 3. Sort 'results' data structure in descending order (sub-process 2) and store in new list 'sorted strings'

# 4. Return 'sorted strings'

VOWELS = ['a', 'e', 'i', 'o', 'u']

def sort_by_consonant_count(str_list):
    totals = {}
    
    for word in str_list:
        consonant_count = get_adj_consonants(word)
        totals[word] = consonant_count

    return consonant_sort(totals)

# Create sorted list:

# Sort result structure:
# 1. Take data structure with strings and number adjacent consonants as input
# 2. Initialize an empty list 'sorted list'
# 3. Sort list:
#     - Save the first item in the data structure to variable 'highest'
#     - Walk through the data structure, comparing each consonant number to the consonant number of 'highest'
#     - if a consonant number is higher than 'highest', save the item to 'highest'
#         - NOT equal to, though
#     - Once at the end of the list, append 'highest' to 'sorted list'
#     - Delete 'highest' from data structure
#     - Continue until all items have been deleted from data structure is 
# 4. Return list

def consonant_sort(total_dict):
    sorted_list = []

    while True:
        string_data = list(total_dict.items())
        highest = string_data[0]
        for item in string_data:
            if item[1] > highest[1]:
                highest = item
        
        sorted_list.append(highest[0])
        del total_dict[highest[0]]
        
        if not total_dict:
            return sorted_list

def get_adj_consonants(string):
    clean_string = string.replace(' ', '')
    highest_adjacent = 0
    current_counter = 0

    for char in clean_string:
        if char not in VOWELS:
            current_counter += 1
            if current_counter > highest_adjacent:
                highest_adjacent += 1
        else:
            current_counter = 0
    return highest_adjacent if highest_adjacent > 1 else 0

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']