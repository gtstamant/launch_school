data_set = {1, 2, 3, 4, 5}
data_2 = set(data_set)

for item in data_set:
    if item % 2 == 0:
        data_2.remove(item)

data_set = {1, 2, 3, 4, 5}

data_set = {item for item in data_set if item % 2 != 0}
print(data_set)