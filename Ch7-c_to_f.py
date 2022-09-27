def c_to_f(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

temp_c = float(input('Enter temperature in Celsius: '))

c_to_f(temp_c)

raise NotImplementedError
print('{} Fahrenheihtet'.format(c_to_f(temp_c)))