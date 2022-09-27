quarters = int(input()) * 25
dimes = int(input()) * 10
nickels = int(input()) * 5
pennies = int(input())

# First, more complex way
whole_dollars = (quarters + dimes + nickels + pennies) // 100
change = (quarters + dimes + nickels + pennies) % 100
print('Amount: ${}.{:02}'.format(whole_dollars, change))

# Simpler way
total = quarters + dimes + nickels + pennies
print(f'Amount: ${total / 100:.2f}')
