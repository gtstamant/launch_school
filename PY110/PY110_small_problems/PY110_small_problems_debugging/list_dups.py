data = [1, 2, 3, 2, 4, 3]

unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)

print(unique_data)  # The order is not guaranteed to be [1, 2, 3, 4]