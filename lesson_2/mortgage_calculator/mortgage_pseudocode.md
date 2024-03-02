# Mortgage Calculator

## Casual Pseudocode

Given:
- a loan amount
- an APR
- a loan duration

Calculate loan duration in months:
- convert loan duration to months
- return loan duration in months

Calculate the monthly interest rate:
- divide the annual percentage rate by 12
- return the monthly percentage rate

## Formal Pseudocode

START

PRINT "Please enter a loan amount in USD"
SET loan_amount = user input loan amount

PRINT "Please enter a duration in years"
SET loan_duration = user input loan duration

SET monthly_loan_duration = loan_duration * 12

SET monthly_payment = loan_amount * (monthly_interest / (1 - (1 + monthly_interest) ** (- monthly_loan_duration)))

PRINT "A loan of loan_duration will require x monthly payments of monthly_payment"
