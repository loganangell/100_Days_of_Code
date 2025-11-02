from state_taxes import lottery_tax_rates

# Define lottery calculation parameters
def calculate_lottery_payments(jackpot, state_tax):
    lump_sum = jackpot * 0.4725
    federal_withholding = lump_sum * 0.37
    state_witholding = lump_sum * state_tax
    return lump_sum - federal_withholding - state_witholding

# Program execution

print() # For formatting only
print("Welcome to the Lottery Payment Calculator!")
print("-" * 64)

while True:
    try:
        j = float(input('Enter a jackpot amount ($): '))
        
        # Validate jackpot amount
        if j <= 0:
            print('The jackpot amount must be greater than 0. Please try again.')
            continue
        else:
            while True:
                state_code = input('Enter your two-letter state code (e.g. WV for West Virginia): ').strip().upper()
                if state_code in ['AL', 'AK', 'HI', 'NV', 'UT']:
                    print(f'{lottery_tax_rates[state_code]['name']} does not allow lottery play. Please try again.')
                    print('')# For formatting only
                elif state_code not in lottery_tax_rates:
                    print('Invalid state code. Please try again.')
                    print('')# For formatting only
                else:
                    s = lottery_tax_rates[state_code]['rate_pct'] / 100
                    payout = calculate_lottery_payments(j, s)
                    break
            break  # Exit the main loop after valid state code is entered
    
    except ValueError:
        print('Invalid input. Please enter a numeric value for the jackpot amount.')
        continue

# Statement Variables
l = j * 0.4725
f = l * 0.37
st = l * s

# Output calculations:
print(' ') # For formatting only
print('Lottery Payment Breakdown:')
print('-' * 63)
print(f"""
      {'Jackpot Amount:':<35}${j:>15,.0f}
      {'Lump Sum Amount:':<35}${l:>15,.0f}
      {'Federal Withholding (37%):':<35}${f:>15,.0f}
      {f'{lottery_tax_rates[state_code]['name']} Withholding ({lottery_tax_rates[state_code]["rate_pct"]}%):':<35}${st:>15,.0f}
      {'Winnings after Taxes:':<35}${payout:>15,.0f}
        """)

print('-' * 63)