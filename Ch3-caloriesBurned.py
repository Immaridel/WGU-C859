
'''
https://learn.zybooks.com/zybook/WGUC859v4/chapter/3/section/13

Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184
Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184

The following equations estimate the calories burned when exercising (source):

Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184
Men: Calories = ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184

Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes),
respectively. Output calories burned for women and men.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
    print('Men: {:.2f} calories'.format(calories_man))

Ex: If the input is:

49
155
148
60

Then the output is:

Women: 580.94 calories
Men: 891.47 calories

'''
''' This code was incorrect due to white spaces and the presence of questions in the Input, but it's worth keeping to see.
age = int(input("How old are you? "))
weight = int(input("What is your current weight? "))
hRate = int(input("What is your heart rate? "))
time = int(input("How long did you work out? "))

calories_women = ((age * 0.074) - (weight * 0.05741) + (hRate * 0.4472) - 20.4022) * time / 4.184
calories_men = ((age * 0.2017) + (weight * 0.09036) + (hRate * 0.6309) - 55.0969) * time / 4.184

print("\nWomen = ", '{:.2f} calories'.format(calories_women))
print("Men = ", '{:.2f} calories'.format(calories_men))
'''


''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

age = int(input())
weight = int(input())
hRate = int(input())
time = int(input())

calories_women = ((age * 0.074) - (weight * 0.05741) + (hRate * 0.4472) - 20.4022) * time / 4.184
calories_men = ((age * 0.2017) + (weight * 0.09036) + (hRate * 0.6309) - 55.0969) * time / 4.184

print("Women:", '{:.2f} calories'.format(calories_women))
print("Men:", '{:.2f} calories'.format(calories_men))