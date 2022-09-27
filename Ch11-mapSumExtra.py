user_input = input()
test_grades = list(map(int, user_input.split()))
# test_grades is an integer list of test scores

# Initialize 0 before your loop
sum_extra = 0

for i in range(len(test_grades)):
    if test_grades[i] > 100:
        sums = test_grades[i] - 100
        sum_extra = sum_extra + sums

print('Sum extra:', sum_extra)
