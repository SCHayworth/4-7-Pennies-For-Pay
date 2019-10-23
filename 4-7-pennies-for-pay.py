# Program 4-7 Pennies For Pay
# Shaun Hayworth
# CIS 2
# 10-22-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-7-Pennies-For-Pay

# Asks the user for a number of days, and calculates their salary over that time based on doubling the amount of pennies paid per day.
# Displays the value of their salary in dollars each day, and a total amount over the provided span of days.

# Initialize the DOLLAR_SIGN string constant.
# This is so that later f-strings can be easily formatted without the need for awkward tabs in output statements.
DOLLAR_SIGN = '$'

# Initialize the pennies variable at 0
pennies = 0

# Initialize value variable at 0.0
value = 0.0

# Initialize the total_salary accumulator at 0.0
total_salary = 0.0

# Initialize the header string
# Change this to adjust header layout
header = '''
Day                  Pennies
----------------------------
'''

# Prompt user for the number of days to compound pennies.
days = int(input('Enter the number of days: '))

# Print header
print(header)

# Check if the number of days is 0
if days == 0:

    # Prints the day and value of 0 pennies.
    print(f'{days:<5}${value:>15.2f}')

    # Prints the total salary of $0.0 and ends the program
    print(f'The total salary for {days} is: ${total_salary:.2f}')
else:

    # Sets pennies to 1
    pennies = 1

    # Loops for the number of specified days
    for time in range(1, days + 1):

        # Calculates the dollar value of the current number of pennies
        value = pennies / 100

        # Prints the day and the value
        print(f'{time:<5}${value:>15.2f}')

        # Double the amount of pennies
        pennies *= 2

        # Adds the current value to total_salary
        total_salary += value

    # Prints the total_salary and ends the program
    print(f'The total salary for {days} is: ${total_salary:.2f}')
