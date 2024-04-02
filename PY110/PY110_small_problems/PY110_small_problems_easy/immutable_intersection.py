def find_intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

print(find_intersection([2,4,6,8], [1,3,5,7,8]))