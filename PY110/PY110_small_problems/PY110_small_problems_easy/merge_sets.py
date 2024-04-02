def merge_sets(list1, list2):
    return set(list1) | set(list2)

print(merge_sets([3,5,7,9], [5,7,11,13]))
# {3, 5, 7, 9, 11, 13}