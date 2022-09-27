"""
200000
210000
"""
current_price = int(input())
last_months_price = int(input())

print('This house is ${}. The change is ${} since last month.'.format(current_price, (current_price - last_months_price)))
print('The estimated monthly mortgage is ${:.2f}.'.format((current_price * 0.051) / 12))