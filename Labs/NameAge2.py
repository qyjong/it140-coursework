'''
Jon Hoover
Introduction to Scripting
IT-140-X2971
21EW2
October 27, 2021
'''

# The following program will ask the user for their name and age, then return the year they were born.
# For more accurate results, it will ask the user if they were born before today's date.

import datetime

user_name = input('What is your name? ')
user_age = int(input('How old are you? '))
today = datetime.date.today() # Get today's date.
todays_date = today.strftime('%b %d') # Format today's date as Month and Day.
year_is_valid = False # Make while loop true, until they answer yes or no correctly.
user_year_born = 2999 # Initialize year born.

while not year_is_valid:

    born_before_today = input('Were you born before ' + todays_date + '? ')

    if born_before_today.lower() == 'y' or born_before_today.lower() == 'yes':
        user_year_born = str(today.year - user_age)
        year_is_valid = True # Exit while loop
    elif born_before_today.lower() == 'n' or born_before_today.lower() == 'no':
        user_year_born = str(today.year - (user_age + 1)) # Adjust the year by 1, due to their not having their
                                                          # birthday yet, this year.
        year_is_valid = True # Exit while loop
    else:
        print('Please enter \'yes\' or \'no\'') # Asks the user to please enter yes or no, to continue. Loops back.

print(user_name + ', you were born in the year ' + user_year_born + '.')
