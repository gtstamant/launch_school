def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)

print(unique_from_first([3,6,9,12], [6,12,15,18]))
# {9, 3}