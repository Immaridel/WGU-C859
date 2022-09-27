"""
8.3
10.4
5.0
4.8
"""
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num_prod = num1 * num2 * num3 * num4
num_avg = (num1 + num2 + num3 + num4) / 4
print('{:.0f} {:.0f}'.format(round(num_prod), (round(num_avg))))
print('{:.3f} {:.3f}'.format(float(num_prod), (float(num_avg))))
