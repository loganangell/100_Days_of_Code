# Define calculation parameters
def calculate_monthly_loan_payment(principal, annual_interest_rate, months):
    i = (annual_interest_rate / 100) / 12
    n = months
    return principal * (i * (1 + i)**n) / ((1 + i)**n - 1)

# Input loan request
loan_amount = int(input('Enter the loan request amount ($): '))
rate = float(input('Enter the annual interest rate (%): '))
months = int(input('Enter the loan term in months: '))

# Calculate payment information
monthly_payment = calculate_monthly_loan_payment(loan_amount, rate, months)

# Output calculation
print(f'The monthly loan payment is: ${monthly_payment:,.2f}.')