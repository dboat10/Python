# Date: September 4th, 2022,
# Description: Working with Dictionaries.

# This block of code prints a welcome message and short dashes for formatting to the console, It also initializes the
# dictionary of countries and their capital city to the variable countries.

print('\t\tCountries and their capital city')
print('\t----------------------------------------')
print()
countries = {'Ghana': 'Accra',
             'Burkina Faso': 'Ouagadougou',
             'Cameroon': 'Yaounde',
             'Canada': 'Ottawa',
             'China': 'Beijing',
             'Colombia': 'Bogota',
             'Cuba': 'Havana',
             'Costa Rica': 'San Jose',
             'Gabon': 'Libreville',
             'Gambia': 'Banjul',
             'Uganda': 'Kampala',
             'Ukraine': 'Kyiv or Kiev',
             'United Arab Emirates': 'Abu Dhabi',
             'United Kingdom': 'London',
             'United States': 'Washington D.C.',
             'Uruguay': 'Montevideo',
             'Uzbekistan': 'Tashkent',
             'Vanuatu': 'Port Vila',
             }

# This block of code displays a header and all the key-value pairs stored in the dictionary by iterating
# over the dictionary till the last key is displayed.

print('Country : Capital City\n-----------------------')
for country, capital in countries.items():
    print('{} : {}'.format(country, capital))
print()

# This block of code prompts the user to input data, takes that data and evaluates against the keys in the dictionary
# to check if there is a match. When the user data matches a key in the dictionary, the associated value is then printed
# out within a context string to the console, else a not exist message is displayed.

message = input('Please select a country: ')
for key, value in countries.items():
    if message.title() == key:
        print()
        print('The capital city of {} is {}'.format(key, value))
        break
else:
    print()
    print(message.title(), 'does not exit in dictionary.')
