# 100 Day Coding Challenge - Day 7: Password Generator

## Introduction
While creating a new account today, I realized I needed a strong, unique password to avoid reusing the same one across multiple platforms—a common habit that increases the risk of hackers accessing multiple accounts. Online platforms have tools to create unique, random passwords that can be used. However, these online sources may track a user’s data or retain logs which could potentially compromise the security of the passwords generated. To address this concern, I decided to develop a local password generator which gives me full control over the passwords I create.

## Background

This project creates a simple password generator used to generate a local, strong password assembled by numbers, letters, and symbols leveraging from Python's ```random``` and ```string```. The project ensures that the passwords generated are created and displayed locally. 

## Tools I Used

* <b> Python </b> - the foundation of my project, used for data extraction via API requests, data cleaning, and visualization.
* <b> VSCode </b> - the code editor for developing and managing the project environment.
* <b> Terminal </b> - used for direct script execution and environment control to ensure seamless interaction between the code and system.
* <b> Git and Github </b> - Essential for version control, project tracking, and collaboration.

## The Analysis

```Python
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
            another_password = input('Would you like to generate another password? (yes/no): ').strip().lower() # ensure input is case insensitive and no leading/trailing spaces
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
```
The project was designed to focus on simplicity, user control, and security. The program follows a protocol with a clear sequence of operations to ensure flexibility during password creation:
* <b> User Input </b>: Prompts the user to specify a password length, ranging from 8 to 32 characters.
* <b> Password Characters </b>: Generates a random combination of letters, numbers, and special symbols, which ensures unpredictability.
* <b> Data Privacy </b>: The generated passwords are not stored or saved after display which reinforces confidentiality.
* <b> Repeat Functionality </b>: Allows users to develop multiple passwords without restarting the application.
* <b> Input Validation </b>: The program detects invalid entries and provides feedback requesting correct input.
* <b> Program Flow </b>: The program continues to run and reset automatically until the user exits the program.

## Conclusion

This simple yet effective password generator allows for flexibility and security when generating a password while ensuring input validation and flow. Future projects using this program can be streamlined for:
* Developing a password strength meter
* Allow a user to customize their character sets
* Clipboard integration
* Machine learning projects for strength predicition and diversity