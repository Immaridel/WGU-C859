import math

ppl = int(input())

avg_pcs = 2
avg_slc = 12
avg_prc = 14.95
total_slices = ppl * avg_pcs
pizzas = math.ceil(total_slices / avg_slc)
cost = avg_prc * pizzas

print('Pizzas: {}'.format(pizzas))
print('Cost: ${:.2f}'.format(cost))
