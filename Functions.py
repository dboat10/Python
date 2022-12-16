# Date: September 18th, 2022
# Description: This program converts miles to kilometers.

# This function takes input from the user, then uses the conversion value to convert the input from miles to kilometers.
def distance():

    trip = {'miles': mile, 'kilometers': kilometer}

    return trip


# This block of code looks out for invalid values passed by the user, then prompts them to provide a valid figure or
# a number greater than zero. When the evaluation is false the process begins and the data from the user is
# converted from miles to kilometers.
while True:
    print()
    print('\tPlease enter your details below.')
    print('---------------------------------------')
    try:
        mile = float(input('How many miles driven?: '))
    except ValueError:
        print('Please enter numbers only')
        continue
    if mile <= 0:
        print('Please enter a number greater than zero')
        continue
    if mile > 0:
        conversion = 1.60934
        kilometer = mile * conversion
        print(mile, 'miles is equivalent to', kilometer, 'kilometers')
        break
print()
print("\tToday's Road Tip \n Do not drink and drive!")  # This line prints a tip of the day message to the user.
