# Ask user for two numbers
# Validate input
# Ask user for operation
# Validate input
# Perform and return operation
# Print result

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_number(num_call):
    prompt(f"What's the {num_call} number?")
    number = input()
    while invalid_number(number):
        prompt("Hmm... that doesn't look like a valid number.")
        number = input()
    return number

def get_operation():
    prompt("""What operation would you like to perform
'Type 1 to add, 2 to subtract, 3 to multiply, 4 to divide""")
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()
    return operation

def get_user_choice():
    user_choice = input()
    while user_choice not in ['y', 'Y', 'n', 'N']:
        print("Sorry, that's not a valid input!")
        user_choice = input()
    return user_choice

def perform_operation(num1, num2, operation):
    match operation:
        case '1':
            output = float(num1) + float(num2)
        case '2':
            output = float(num1) - float(num2)
        case '3':
            output = float(num1) * float(num2)
        case '4':
            output = float(num1) / float(num2)
    prompt(f'The result is: {output}.\n')

def run_calculator():
    prompt('Welcome to Calculator!\n')
    while True:
        number_1 = get_number('first')
        number_2 = get_number('second')
        chosen_operation = get_operation()
        perform_operation(number_1, number_2, chosen_operation)
        prompt('Would you like to perform another operation? y/n.')
        continue_op = get_user_choice()
        if continue_op == 'n':
            prompt('Thanks for calculating! See you later.\n')
            break

run_calculator()