"""
## Problem ##


"""

# def clean_word(word):
#     clean_word = ''
#     for char in word:
#         if char.isalpha():
#             clean_word += char
#     return clean_word

# def word_sizes(string):
#     results = {}
#     word_list = string.split()
#     clean_list = []

#     for word in word_list:
#         clean_list.append(clean_word(word))

#     for word in clean_list:
#         results[len(word)] = results.get(len(word), 0) + 1
    
#     return results

def word_sizes(string):
    results = {}
    
    for word in string.split():
        clean_word = ''.join(char for char in word if char.isalpha())
        length = len(clean_word)
        results[length] = results.get(length, 0) + 1
    
    return results

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# Without dict.get method

# def word_sizes(string):
#     results = {}
#     word_list = string.split()

#     for word in word_list:
#         if len(word) not in results:
#             results[len(word)] = 1
#         else:
#             results[len(word)] += 1
    
#     return results