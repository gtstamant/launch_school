# def keep_keys(dictionary, keys):
#     return {key: value for key, value in dictionary.items()
#             if key in keys}

def keep_keys(dictionary, keys):
    return {key: dictionary[key] for key in keys
            if key in dictionary}

print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}