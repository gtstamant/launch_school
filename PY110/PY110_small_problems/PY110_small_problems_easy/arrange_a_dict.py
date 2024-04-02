# def order_by_value(dictionary):
#    keys = sorted(list(dictionary.keys()), key=dictionary.get)
#    return keys

def order_by_value(dictionary):
    sorted_items = sorted(dictionary.items(), key=get_val)
    return [key for key, _ in sorted_items]

def get_val(lst):
    return lst[1]


print(order_by_value({'p': 8, 'q': 2, 'r': 6}))