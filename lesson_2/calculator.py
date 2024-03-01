# Ask user for two numbers
# Validate input
# Ask user for operation
# Validate input
# Perform and return operation
# Print result

print('Welcome to Calculator!')

def get_number(num_call):
    while True:
        try:
            num = float(input(f'What is the {num_call} number? '))
            return num
        except ValueError:
            print("That's not a number!")

def get_operation():
    valid_input = [1, 2, 3, 4]
    while True:
        try:
            operation = int(input(
                'What operation would you like to perform? \n'
                'Type 1 to add, 2 to subtract, 3 to multiply, 4 to divide \n'
            ))
            if operation in valid_input: 
                return operation
            else:
                print('Invalid input! Choose between numbers 1 - 4')
        except ValueError:
            print('Invalid input! Choose between numbers 1 - 4')

def perform_operation(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    if operation == 2:
        return num1 - num2
    if operation == 3:
        return num1 * num2
    if operation == 4:
        return num1 / num2
    
num1 = get_number('first')
num2 = get_number('second')
operation = get_operation()
print(perform_operation(num1, num2, operation))





