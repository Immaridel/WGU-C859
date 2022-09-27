'''
Create a different version of the program that:

    Calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
    Repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number is less than 1. Hint: Use a while loop that will execute as long as num_rolls is greater than 1.
    Prints a histogram in which the total number of times the dice rolls equals each possible value is displayed by printing a character, such as *, that number of times. The following provides an example:

Dice roll histogram:

2s:  **
3s:  ****
4s:  ***
5s:  ********
6s:  *************
7s:  *****************
8s:  *************
9s:  *********
10s: **********
11s: *****
12s: **
'''


import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll {} is {} ({} + {})'.format(i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')