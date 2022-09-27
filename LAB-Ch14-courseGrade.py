import os

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, 'report.txt')
if os.path.isfile(file):
    os.remove(file)

midterm1 = int()
midterm2 = int()
fgrade = int()
counter = 0

with open(input()) as f:
    raw = f.readlines()
    for i in raw:
        line = i.strip().split('\t')
        grade = (int(line[2]) + int(line[3]) + int(line[4])) / 3
        counter += 1
        midterm1 += int(line[2])
        midterm2 += int(line[3])
        fgrade += int(line[4])
        if grade >= 90:
            letter = "A"
        elif 80 <= grade < 90:
            letter = "B"
        elif 70 <= grade < 80:
            letter = "C"
        elif 60 <= grade < 70:
            letter = "D"
        elif grade < 60:
            letter = "F"
        with open('report.txt', 'a') as w:
            line_new = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(line[0], line[1], line[2], line[3], line[4], letter)
            w.write(line_new)

    with open('report.txt', 'a') as w:
        midavg1 = midterm1 / counter
        midavg2 = midterm2 / counter
        favg = fgrade / counter
        last_line = '\nAverages: midterm1 {:.2f}, midterm2 {:.2f}, final {:.2f}\n'.format(midavg1, midavg2, favg)
        w.write(last_line)

