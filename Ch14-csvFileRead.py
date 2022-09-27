import csv

# Dictionary that maps student names to a list of scores
grades = {}

# Use with statement to guarantee file closure
with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    first_row = True
    for row in grades_reader:
        # Skip the first row with column names
        if first_row:
            first_row = False
            continue

        ## Calculate final student grade ##

        name = row[0]

        # Convert score strings into floats
        scores = [float(cell) for cell in row[1:]]

        hw1_weighted = scores[0]/10 * 0.05
        hw2_weighted = scores[1]/10 * 0.05
        mid_weighted = scores[2]/100 * 0.40
        fin_weighted = scores[3]/100 * 0.50

        grades[name] = (hw1_weighted + hw2_weighted +
                        mid_weighted + fin_weighted) * 100

for student, score in grades.items():
    print('{} earned {:.1f}%'.format(student, score))
