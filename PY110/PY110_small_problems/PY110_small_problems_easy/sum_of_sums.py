# def sum_of_sums(lst):
#     return sum([sum(lst[:idx + 1]) for idx in range(len(lst))])

# def sum_of_sums(lst):
#     lst_of_sums = [sum(lst[:idx + 1]) for idx in range(len(lst))]
#     return sum(lst_of_sums)

# def sum_of_sums(lst):
#     lst_of_sums = []

#     for idx in range(len(lst)):
#         lst_of_sums.append(sum(lst[:idx + 1]))
    
#     return sum(lst_of_sums)

def sum_of_sums(lst):
    running_total = 0 # 3, 8, 10
    total = 0 # 3, 11, 21

    for number in lst:
        running_total += number
        total += running_total
    
    return total

print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35