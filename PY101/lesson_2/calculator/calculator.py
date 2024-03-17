import json

with open('messages.json', 'r') as file:
    message_data = json.load(file)

LANGUAGE = 'en'

def messages(message, lang='en', data=message_data):
    return data[lang][message]

def prompt(message):
    message = messages(message, LANGUAGE)
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_number():
    prompt("GET_NUMBER")
    number = input()
    while invalid_number(number):
        prompt("NUMBER_ERROR")
        number = input()
    return number

def get_operation():
    prompt("GET_OPERATION")
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt("OPERATION_ERROR")
        operation = input()
    return operation

def get_user_choice():
    user_choice = input()
    if not user_choice or user_choice[0].lower() not in ['y', 'n']:
        print("USER_CHOICE_ERROR")
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
    prompt("RESULT")
    print(output)

def run_calculator():
    prompt("WELCOME")
    while True:
        number_1 = get_number()
        number_2 = get_number()
        chosen_operation = get_operation()
        perform_operation(number_1, number_2, chosen_operation)
        prompt("REPEAT")
        continue_op = get_user_choice()
        if continue_op and continue_op[0].lower() == 'n':
            prompt("GOODBYE")
            break

run_calculator()