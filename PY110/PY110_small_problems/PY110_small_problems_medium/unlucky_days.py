from datetime import date

def friday_the_13ths(year):
    total = [True for month in range(1, 13)
             if date(year, month, 13).weekday() == 4]
    
    return len(total)

print(friday_the_13ths(1986))      # 1
print(friday_the_13ths(2015))      # 3
print(friday_the_13ths(2017))      # 2