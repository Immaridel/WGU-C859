mpg = float(input())
gas = float(input())

miles20 = (20 / mpg) * gas
miles75 = (75 / mpg) * gas
miles500 = (500 / mpg) * gas

print('{:.2f} {:.2f} {:.2f}'.format(miles20, miles75, miles500))
