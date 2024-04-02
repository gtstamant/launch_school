def swap_name(str_name):
    name_lst = str_name.split()
    first_name = name_lst[0]
    surname = name_lst[-1]
    middle_names = ' '.join(name_lst[1:-1]).rstrip()

    return f'{surname}, {first_name} {middle_names}'
    
    # return ', '.join(str_name.split()[::-1])

print(swap_name('Joe Roberts'))    # "Roberts, Joe"
print(swap_name('Karl Oskar Henriksson Ragvals'))    # "Ragvals, Karl Oskar Henriksson"