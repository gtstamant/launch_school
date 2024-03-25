'''
Problem:

Input: Requests six numbers from the user through the terminal
Output: Prints a message to terminal stating whether sixth number
appears in previous five

Questions:
- Can we assume the user will input a number?
- Can we assume that number will be an int?
- What about negative numbers/0?

Examples:
- 25, 15, 20, 17, 23, 17
- 25, 15, 20, 17, 23, 18
- None
- '25', … (as strings)
- -25, … (negatives)

Data structure:
- store input in list

Algorithm:

1. Ask user for six numbers (subprocess) and store each in list
2. Check if #6 in #1-5
3. Print result of step two to terminal

** input subprocess **

Input: None (some from user)
Output: Return number list

1. Set variable 'numbers' to empty list
2. Print request for number to user's terminal
- Check whether the length of 'numbers' is equal to 6
- If not, repeat #2
3. Return 'numbers'

'''

def get_user_inputs():
    numbers = []
    ordinals = ['1st', 
                '2nd', 
                '3rd', 
                '4th', 
                '5th', 
                'last',
    ]

    for index in range(len(ordinals)):
        numbers.append(
            input(f'Enter the {ordinals[index]} number: '))
    
    return numbers

def search_for_sixth():
    numbers = get_user_inputs()
    sixth_num = numbers[5]
    five_nums = numbers[:-1]
    
    if sixth_num in five_nums:
        print(f'{sixth_num} is in {",".join(five_nums)}.')
    else:
        print(f"{sixth_num} isn't in {','.join(five_nums)}.")

# Further exploration

def does_satisfy_condition(condition):
    numbers = get_user_inputs()
    for number in numbers:
        if condition(int(number)):
            print(f'{number} satisfies the condition!')
            return True
        print(f'No numbers satisfy the condition.')
        return False

def compare_25(num):
    return num > 25

does_satisfy_condition(compare_25)