## Nested data structures ##

# 1 - What will happen when we run this code?

import copy

orig = [[1, 2], 3, 4] # variables => elements, 
dup = copy.copy(orig) # method

print(orig is dup) 
print(orig == dup)
orig[2] = 44 # Index 3, element reassignment
print(dup) # Why doesn't it change

print(orig[0] is dup[0]) # same location
orig[0][1] = 22
print(dup[0]) # why does this change

## Variable scoping ##

# 1

outer_var = 15

def my_func():
    print(outer_var)

my_func()  

# Output: 15

# 2 - note that here declaring my_var in the local scope shadows, creating problem
## is my ## does anything print
my_var = "Hello"

def my_func():
    my_vara = my_var + " world"
    return my_vara

my_var = my_func()
print(my_var)

# 3 - What happens when we run this code?

def foo():
    def bar():
        print('BAR')

    bar()

foo()
bar()

# 4 — What happens when we run this code, and why?

def outer():
    def inner1():
        def inner2():
            global foo
            foo = 3
            print(f"inner2 -> {foo}") # with id {id(foo)}"

        foo = 2
        inner2()
        print(f"inner1 -> {foo}") # with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo}") # with id {id(foo)}")

outer()

# 5

a = 1

def foo():
    b = 2

    def bar():
        c = 3
        print(a)
        print(b)
        print(c)

    bar()

    print(a)
    print(b)
    print(c)

foo()

# 6

def my_func():
    x = 15

    def inner_func1():
        x = 25 # non-local version
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()


## Method chaining

# 1

def do_something(dictionary): # parameter as local variable
    return sorted(dictionary.keys())[1].upper() # what is returned here

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict)) # references to objects


## Explain what this code will do and why

# 1

def foo(s):
    s = s + " world"
    return s

str_val = "hello"
foo(str_val)

# 2

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

print(bar(foo()))

# 3

if False:
    greeting = "hello world"

print(greeting)

## Mutation

# 1

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# 2

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)
print(munsters)