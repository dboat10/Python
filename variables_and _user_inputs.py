# Date: August 28, 2022,
# Description: This program initializes a variable, takes input from users then calculates and displays a total price.

# This block of code, initializes a values to variables , it also seeks input from users with a prompt message.
unit_cost = 0.87
print('--------- Welcome to Oscar Fibre Installation LLC ---------')
name = input('Please enter your company name\n')  # Prompting the user to enter information
length = int(input(f'Hi {name}, how many feet of cable do you need?\n'))  # Prompting the user to enter information

# This block of code evaluates the input given by the user to determine if it meets any of the conditions specified
# in the if statements then applies the right discount price to the user's purchase.
if length > 100 <= 250:
    unit_cost = 0.80
    total_cost = length * unit_cost
    if length > 250 <= 500:
        unit_cost = 0.70
        total_cost = length * unit_cost
    if length > 500:
        unit_cost = 0.50
        total_cost = length * unit_cost
else:
    total_cost = length * unit_cost

# This line of code displays the given input, calculated price and additional message back to the user.
print(f'Thank you, {name} the total cost for {length}ft. of cable is ${total_cost:,.2f}')
