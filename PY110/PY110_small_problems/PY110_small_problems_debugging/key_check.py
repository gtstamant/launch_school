# def get_key_value(my_dict, key):
#     try:
#         if my_dict[key]:
#             return my_dict[key]
#     except KeyError:
#         return None
    
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))