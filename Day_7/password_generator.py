import random
import string

# Define function to generate password
def password_information(length):
    """Generates a random password using different characters"""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Execution of program

while True:
    try:
        length = int(input('Enter the desired password length (between 8 to 32 characters): '))

        # Length Validation
        if length < 8 or length > 32:
            print('The password length must be between 8 and 32 characters. Please try again.')
            continue
        else:
            password = password_information(length)
            print(f'\n Password: {password}\n')

        # Validate request for another password
        while True:
            another_password = input('Would you like to generate another password? (yes/no): ').strip().lower()
            if another_password == 'yes':
                print('') # just for formatting
                break
            elif another_password == 'no':
                print('') # just for formatting
                print('Thank you for using the password generator. Stay safe in cyberspace!')
                exit() # exit the program
            else:
                print('Invalid input. Please enter "yes" or "no".')
                print('') # just for formatting

    except ValueError:
        print('Invalid input. Please enter a numeric value for the password length.')
        continue