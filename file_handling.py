# Date: September 25th, 2022
# Summary: Handling files in python

import os  # This is a built-in method that can be imported into a script file to help with file verification.

# This block of code takes input from the user.
file_directory = input('Please enter file directory: ')
filename = input('Please enter file name: ')
name = input('Please enter your name: ')
address = input('Please enter your address: ')
cell = input('Please enter you phone number: ')

# This block of code verifies that the file directory is valid, then creates a file by writing the collected data from
# the user into the provided file directory.
if os.path.isdir(file_directory):
    with open(filename, 'w') as f:
        f.write(name + ', ' + address + ', ' + cell)
        print()
        print('-----------------------------')

# This block of code opens the created file to read the data then prints the data in the file onto the console.
with open(filename, 'r') as f:
    data = f.read()
    print(data)

