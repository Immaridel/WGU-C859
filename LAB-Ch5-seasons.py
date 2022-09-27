'''
Write a program that takes a date as input and outputs the date's season.
The input is a string to represent the month and an int to represent the day.

The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
'''

input_month = input()
input_day = int(input())

spring = ['april', 'may']
summer = ['july', 'august']
autumn = ['october', 'november']
winter = ['january', 'february']

short_months = ['february', 'april', 'june', 'september', 'november']

if (((input_month.lower() == 'february') and ((input_day <= 0) or (input_day > 28))) or
        ((input_month.lower() in short_months) and ((input_day <= 0) or (input_day > 30)))
        or ((input_day <= 0) or (input_day > 31))):
    print('Invalid')
    exit()

if (input_month.lower() == 'march' and input_day >= 20) or \
        (input_month.lower() == 'june' and input_day <= 20) or \
        (input_month.lower() in spring):
    season = 'Spring'
elif (input_month.lower() == 'june' and input_day >= 21) or \
        (input_month.lower() == 'september' and input_day <= 20) or \
        (input_month.lower() in summer):
    season = 'Summer'
elif (input_month.lower() == 'september' and input_day >= 22) or \
        (input_month.lower() == 'december' and input_day <= 20) or \
        (input_month.lower() in autumn):
    season = 'Autumn'
elif (input_month.lower() == 'december' and input_day >= 21) or \
        (input_month.lower() == 'march' and input_day <= 19) or \
        (input_month.lower() in winter):
    season = 'Winter'
else:
    print('Invalid')
    exit()

print(season)