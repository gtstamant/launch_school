### Question 1 ###

# num = 5

# def my_func():
#     print(num)

# my_func() # 5

### Question 2 ###

# num = 5

# def my_func():
#     num = 10

# my_func() # nothing
# print(num) # 5

### Question 3 ###

# num = 5

# def my_func():
#     global num
#     num = 10

# my_func() # nothing
# print(num) # 10

### Question 4 ###

# def outer():
#     outer_var = 'Hello'

#     def inner():
#         inner_var = 'World'
#         print(outer_var, inner_var)
    
#     inner() # Hello, World

# outer() # Nothing

### Question 5 ###

# def my_func():
#     num = 10

# my_func() # Nothing
# print(num) # NameError: num is not defined

### Question 6 ###

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1() 
    inner_func2()

my_func() # Inner 1: 25 ; Inner 2: 15