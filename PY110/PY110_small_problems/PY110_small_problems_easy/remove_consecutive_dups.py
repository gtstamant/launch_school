# def unique_sequence(seq):
#     return list(set(seq))
# def unique_sequence(seq):
#     if not seq:
#         return []
    
#     unique = [seq[0]]
#     for value in seq[1:]:
#         if value != unique[-1]:
#             unique.append(value)
    
#     return unique

def unique_sequence(seq):
    return [value for idx, value in enumerate(seq)
            if idx == 0 or value != seq[idx - 1] ]

print(unique_sequence([1, 1, 2, 3, 3, 3, 4, 5, 5, 6]))
# [1, 2, 3, 4, 5, 6]