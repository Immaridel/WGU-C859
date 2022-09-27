cities = {
    'Nairobi': 958,
    'London': 438,
    'Chicago': 584,
    'Paris': 550,
    'Austin': 309,
    'Toronto': 3435,
}

#best = ''
distance = 0
for miles in cities:
    #print(cities[miles])
    if cities[miles] > distance:
        best = miles
        distance = cities[miles]
print(best, distance)