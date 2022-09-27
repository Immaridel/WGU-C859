def get_weight():
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

user_input = ''
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as fuck:
        print(fuck)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")