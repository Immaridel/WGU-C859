grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print('Homework {}: {}'.format(hw, score))

        print('Midterm: {}'.format(midterm))
        print('Final: {}'.format(final))

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        print('Final percentage: {:.1f}%'.format(100*(total_points / 500.0)))

    user_input = input('Enter student name: ')