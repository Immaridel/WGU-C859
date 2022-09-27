#Program to calculate statistics from student test scores.
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(num_midterm_scores, 'students took the midterm.')
print(num_final_scores, 'students took the final.')

#Calculate the number of students that took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(dropped_students, 'students must have dropped the class.')

lowest_final = min(final_scores)
highest_final = max(final_scores)

print('\nFinal scores ranged from', lowest_final, 'to', highest_final)

# Calculate the average midterm and final scores
# Hint: Sum the midterm scores and divide by number of midterm takers
#       Repeat for the final
print('Average midterm score:', '{:.2f}'.format(sum(midterm_scores) / len(midterm_scores)))
print('Average final score:', '{:.2f}'.format(sum(final_scores) / len(final_scores)))