VOWELS = 'aeiou'

# def get_no_vowel_str(string):
#     no_vowels = ''
#     for char in string:
#         if char.casefold() not in VOWELS:
#             no_vowels += char
    
#     return no_vowels

def get_no_vowel_str(string):
    return (''.join([char for char in string
                     if char.casefold() not in VOWELS]))

def remove_vowels(lst_of_str):
    return [get_no_vowel_str(string) for string
            in lst_of_str]

print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']) == ['bcdfghjklmnpqrstvwxyz'])
print(remove_vowels(['green', 'YELLOW', 'black', 'white']) == ['grn', 'YLLW', 'blck', 'wht'])
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']) == ['BC', '', 'XYZ'])