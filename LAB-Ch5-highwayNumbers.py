'''
Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens
(like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by
the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.

Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary
highway it serves. Also indicate if the (primary) highway runs north/south or east/west.
'''


highway_number = int(input())

if highway_number % 2 != 0:
    direction = 'north/south'
else:
    direction = 'east/west'

if highway_number == 0:
    print('{} is not a valid interstate highway number.'.format(highway_number))
    exit()
elif len(str(highway_number)) <= 2:
    htype = 'primary'
    print('I-{} is {}, going {}.'.format(highway_number, htype, direction))
    exit()
elif len(str(highway_number)) > 3:
    print('{} is not a valid interstate highway number.'.format(highway_number))
    exit()
else:
    htype = 'auxiliary'
    highway_ones = highway_number % 10
    highway_tens = (highway_number // 10) % 10
    if (highway_ones == 0) and (highway_tens == 0):
        print('{} is not a valid interstate highway number.'.format(highway_number))
        exit()
    elif highway_tens == 0:
        highway_name = repr(highway_ones)
    else:
        highway_name = repr(highway_tens) + repr(highway_ones)
    print('I-{} is {}, serving I-{}, going {}.'.format(highway_number, htype, highway_name, direction))