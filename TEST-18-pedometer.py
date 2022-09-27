def steps_to_miles(steps):
    if steps < 0:
        raise ValueError('Exception: Negative step count entered.')
    else:
        miles = steps / 2000
    return miles


if __name__ == '__main__':
    try:
        steps = int(input())
        miles = steps_to_miles(steps)
        print(f'{miles:.2f}')

    except ValueError as error:
        print(error)
