is_leap_year = False

input_year = int(input())

year_ones = input_year % 10
year_tens = (input_year // 10) % 10

if year_ones == 0 and year_tens == 0:
    if (input_year % 400) > 0:
        print('{} - not a leap year'.format(input_year))
        exit()
    else:
        print('{} - leap year'.format(input_year))
elif (input_year % 4) > 0:
    print('{} - not a leap year'.format(input_year))
    exit()
else:
    print('{} - leap year'.format(input_year))