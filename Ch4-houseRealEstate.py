# Concatenating lists
house_prices = [380000, 900000, 875000] + [225000]
print('There are', len(house_prices), 'prices in the list.')
# Finding min, max
print('Cheapest house:', min(house_prices))
print('Most expensive house:', max(house_prices))
print('Average house price:', sum(house_prices) / len(house_prices))