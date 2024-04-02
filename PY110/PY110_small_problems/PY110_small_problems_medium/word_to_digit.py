# def word_to_digit(message):
#     message = message.split()
#     for idx, word in enumerate(message):
#         match word:
#             case 'zero': 
#                 message[idx] = '0'
#             case 'one':
#                 message[idx] = '1'
#             case 'two':
#                 message[idx] = '2'
#             case 'three':
#                 message[idx] = '3'
#             case 'four':
#                 message[idx] = '4'
#             case 'five':
#                 message[idx] = '5'
#             case 'six':
#                 message[idx] = '6'
#             case 'seven':
#                 message[idx] = '7'
#             case 'eight':
#                 message[idx] = '8'
#             case 'nine':
#                 message[idx] = '9'
#     return ' '.join(message)

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

import string

def word_to_digit(message):
    conversion = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    # split_message = message.split()
    # for idx, word in enumerate(split_message):
    #     for key, item in conversion.items():
    #         if key in word:
    #             split_message[idx] = item + word[-1]
    
    # return ' '.join(split_message)
    result = []
    split_message = message.split()
    for word in split_message:
        if word[-1] in string.punctuation:
            new_word = conversion.get(word[:-1], word[:-1]) + word[-1]
        else:
            new_word = conversion.get(word, word)
        result.append(new_word)
    
    return ' '.join(result)

            

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True