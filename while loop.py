# Date: September 11th, 2022
# Description: This program calculates how long an investment takes to double at a given interest rate.


# This block of code prints out a welcome message, instructions and also takes user input.
print("\t\tWelcome to Oscar's Interest Calculator. \n\t\t Please enter investment details below")
print('-------------------------------------------------------')
print()
interestRate = input('Interest Rate: ')
initialInvestment = float(input('Initial Amount: '))
doubledAmount = initialInvestment
year = 0
duration = ''

# This block of code evaluates the variable doubledAmount against initialInvestment multiplied by 2, to check if it
# is less, while that evaluation is true, doubledAmount is calculated and multiplied by the interest rate being
# divided by 100. An extra year is added on until the evaluation becomes false. Then if the amount of year is greater
# than 1 the duration is presented in a plural sentence else is it presented as a singular noun.

while doubledAmount < initialInvestment * 2:
    doubledAmount = doubledAmount + doubledAmount * (float(interestRate) / 100)
    year = float(year) + 1
    if year != 1:
        duration = 'years'
    else:
        duration = 'year'

# After the calculation is done, this line of code prints the values to the console in a human-readable language.

print()  # Prints out an empty line to space out the console output.
print(f'At an annualized interest rate of {interestRate}%, it will take {year} {duration} to double '
      f'${initialInvestment:,.2f} to ${doubledAmount:,.2f}')
print()
print("Thank you for using Oscar's Interest Calculator.\nGood bye!")
