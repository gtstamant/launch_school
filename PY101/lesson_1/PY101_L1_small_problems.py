def century(year):
    str_year = str(year)
    if str_year[-1] == '0':
        century = year // 100
    else:
        century = year // 100 + 1
    
    return f'{century}{get_ordinal_ending(century)}'

def get_ordinal_ending(num):
    str_num = str(num)

    try:
        last_two = str_num[-2:]
    except IndexError:
        last_two = None
    
    if last_two:
        match last_two:
            case '11' | '12' | '13': return 'th'
    
    match str_num[-1]:    
        case '1': return 'st'
        case '2': return 'nd'
        case '3': return 'rd'
        case _  : return 'th'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True  
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True