def invalid_input(amount):
    try:
        float(amount)
    except ValueError:
        return True
    return False

def collect_loan_data():
    print("What is the loan principal in USD? ")  
    principal = input()
    while invalid_input(principal):
        print("Hmmm...please input a valid number!")
    
    print("What is the annual percentage interest? Please input as a percent!")
    annual_interest = input().replace('%', '')
    while invalid_input(annual_interest):
        print("Hmmm...please input a valid percentage!")

    print("What is the loan duration in years?")
    loan_time = input()
    while invalid_input(loan_time):
        print('Hmmm...please input a valid number!')
    
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
    print(f'Your monthly payment is ${monthly_payment:.2f} '
          f'for every month over {duration} months.\n'
          f'Your will pay ${interest_payment:.2f} in total interest.'
    )

def run_calculator():
    print("""Welcome to the mortgage calculator!\n
    Let's start by gathering some details about your loan."""
    )
    principal, apr, duration = collect_loan_data()
    month_rate = monthly_rate(apr)
    month_duration = monthly_duration(duration)
    month_payment = loan_payment(principal, month_rate, month_duration)
    interest = total_interest(principal, month_duration, month_payment)
    display_data(month_duration, month_payment, interest)

run_calculator()