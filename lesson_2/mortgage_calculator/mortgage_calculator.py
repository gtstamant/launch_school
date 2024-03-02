import os
import json

with open('mort_messages.json', 'r') as message_text:
    message_data = json.load(message_text)

def messages(message):
    return message_data[message]

def prompt(message):
    print_val = messages(message)
    print(print_val)

def invalid_input(num):
    try:
        num = float(num)
        if num <= 0:
            raise ValueError(f"Value must be > 0: {num}")
    except ValueError:
        return True
    return False

def collect_loan_data():
    prompt("PRINCIPAL")  
    principal = input()
    while invalid_input(principal):
        prompt("INVAL_NUM")
        principal = input()
    
    prompt("APR")
    annual_interest = input().replace('%', '')
    while invalid_input(annual_interest):
        prompt("INVAL_PERC")
        annual_interest = input().replace('%', '')

    prompt("DURATION")
    loan_time = input()
    while invalid_input(loan_time):
        prompt("INVAL_NUM")
        loan_time = input()
    
    principal = float(principal)
    annual_interest = float(annual_interest) / 100
    loan_time = float(loan_time)

    return (principal, annual_interest, loan_time)

def monthly_rate(annual_rate):
    return annual_rate / 12

def monthly_duration(annual_duration):
    return annual_duration * 12

def loan_payment(amount, interest, duration):
    return (
        amount * (interest / (1 - (1 + interest) ** (-duration)))
    )

def total_interest(amount, duration, payments):
    return (duration * payments) - amount

def display_data(duration, monthly_payment, interest_payment):
    data = messages('DATA').format(
        monthly_payment=monthly_payment, 
        duration=duration, 
        interest_payment=interest_payment
    )
    print(data)

def get_user_choice():
    user_choice = input()
    if not user_choice or user_choice[0].lower() not in ['y', 'n']:
        prompt('INVAL_CHOICE')
        user_choice = input()
    return user_choice

def run_calculator():
    prompt('WELCOME')
    while True:
        prompt("START")
        
        principal, apr, duration = collect_loan_data()
        month_rate = monthly_rate(apr)
        month_duration = monthly_duration(duration)
        month_payment = loan_payment(principal, month_rate, month_duration)
        interest = total_interest(principal, month_duration, month_payment)
        
        display_data(month_duration, month_payment, interest)
        prompt('DECISION')
        decision = get_user_choice()
        if decision[0].lower() == 'n':
            prompt('GOODBYE')
            break
        os.system('clear')

run_calculator()