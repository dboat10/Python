# Name: Oscar Boateng Acheampong
# Date: 08/24/2022
# Assignment#: Module 4
# Description: Iterating over tuple elements in default and reverse orders.

# Creating an empty tuples with variable name cars.
cars = ()

# Initiating the variable with tuple elements then print them out to the console.
cars = ("Toyota", "Acura", "Honda", "Alfa Romeo", "Audi", "Volkswagen", "Mercedes", "Bentley", "Buick", "GM",
        "Cadillac", "Chevy", "Chrysler", "Dodge", "Fiat", "Ford", "GMC", "Genesis", "Hyundai", "Infinity",
        "Jaguar", "Jeep", "Kia", "Range Rover", "Tesla")
print(cars)

# This print statement create a new line before and after the dashed lines for readability purposes.
print("\n--------------------------------------------------------\n")

# The for loop statement iterates over the tuple elements from index [0] to index [24] then print out a message with
# each element
for car in cars:
    print(f'My dream car is a BMW not {car}')

# This print statement create a new line before and after the dashed lines for readability purposes.
print("\n--------------------------------------------------------\n")

# This block of code iterates over the tuple elements in reverse order.
for car in reversed(cars):
    print(f'That is a nice {car}')
