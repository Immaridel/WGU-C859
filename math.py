import math

x = float(input())
y = float(input())
z = float(input())

your_value1 = math.pow(x, z)
your_value2 = math.pow(x, (math.pow(y, z)))
your_value3 = math.fabs(x - y)
your_value4 = math.sqrt(math.pow(x, z))


print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))