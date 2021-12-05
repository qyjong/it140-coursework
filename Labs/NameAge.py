
"""
Jon Hoover
Introduction to Scripting
IT-140-X2971
21EW2
October 27, 2021
"""

# The following program will ask the user for their name and age, then return the year they were born.

import datetime

user_name = input('What is your name? ')
user_age = int(input('How old are you? '))
today = datetime.date.today()

user_year_born = str(today.year - user_age)
print(user_name + ', you were born in the year ' + user_year_born + '.')
