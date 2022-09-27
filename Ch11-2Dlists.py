# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        0,
        960,  # Boston-Chicago
        2960 # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        0,
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los-Angeles-Chicago
        0
    ]
]

user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print('Distance: {} miles'.format(distances[int(city1)][int(city2)]))
