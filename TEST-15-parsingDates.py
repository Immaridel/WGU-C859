"""
March 1, 1990
April 2 1995
7/15/20
December 13, 2003
-1
"""

"""
def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input().title().strip('/')
while user_string != "-1":
    date = user_string.split()
    month = date[0].title()
    month_int = get_month_as_int(date[0])
    if (month_int != 0) and ("," in user_string):
        print(f'{get_month_as_int(month)}/{date[1].strip(",")}/{date[2]}')
    user_string = input().title().strip('/')
"""
def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()
while user_string != "-1":
    date = user_string.split()
    if ("/" not in user_string) and ("," in user_string):
        month = date[0].title()
        day = date[1].strip(',')
        year = date[2]
        print(f'{get_month_as_int(month)}/{day}/{year}')
        user_string = input()
    else:
        user_string = input()