"""
Given the code that reads a list of integers, complete the number_guess() function, which should choose a random number
between 1 and 100 by calling random.randint() and then output if the guessed number is too low, too high, or correct.

Import the random module to use the random.seed() and random.randint() functions.

    random.seed(seed_value) seeds the random number generator using the given seed_value.
    random.randint(a, b) returns a random number between a and b (inclusive).

For testing purposes, use the seed value 900, which will cause the computer to choose the same random number every time the program runs.

Ex: If the input is:
    32 45 48 80

the output is:
    32 is too low. Random number was 80.
    45 is too high. Random number was 30.
    48 is correct!
    80 is too low. Random number was 97.

Help on method randint in module random:
    randint(a, b) method of random.Random instance
        Return random integer in range [a, b], including both end points.

Help on method seed in module random:
    seed(a=None, version=2) method of random.Random instance
        Initialize internal state from hashable object.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If *a* is an int, all bits are used.

        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.
"""
import random


def number_guess(num):
        correct = random.randint(1, 100)
        if num > correct:
            print('{} is too high. Random number was {}.'.format(num, correct))
        elif num < correct:
            print('{} is too low. Random number was {}.'.format(num, correct))
        else:
            print('{} is correct!'.format(num))


if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)

    # Convert the string tokens into integers
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)