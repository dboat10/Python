# Date: September 18th, 2022
# Description: This program converts miles to kilometers.

# This function takes input from the user, then uses the conversion value to convert the input from miles to kilometers.
# It then asks the user if they want to make another trip conversion expecting a yes or no answer to embark on another
# operation. when the answer is given, it converts the first letter to lower case then evaluates against the
# specified conditions in the if statement.

def distance():
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
            print()
            question = input("Do you have another trip to convert? Enter Yes or No: ")
            question = question.lower()  # This lines concerts the first letter of the user's answer to lower case.
            if question == 'yes' or question == 'y':
                return distance()  # This lines returns the program to the beginning if the user answers yes.
            if question == 'no' or question == 'n':
                print()
                print("\tToday's Road Tip \n Do not drink and drive!")
                break  # This lines ends the program when the user answers no.


distance()
