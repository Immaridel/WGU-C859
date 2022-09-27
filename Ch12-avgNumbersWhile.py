'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5
'''

values_sum = 0
num_values = 0

curr_value = int(input('Enter a number: '))

try:
    while curr_value > 0:  # Get values until 0 (or less)
        values_sum += curr_value
        num_values += 1
        curr_value = int(input('Enter another number: '))
except:
    print('Average: {:.0f}\n'.format(values_sum / num_values))