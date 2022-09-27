male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

# Use set methods to create sets all_names, neutral_names, and specific_names.

all_names = set.union(male_names, female_names)
neutral_names = set.intersection(male_names, female_names)
specific_names = set.symmetric_difference(male_names, female_names)
female_difference = set.difference(female_names, male_names)
male_difference = set.difference(male_names, female_names)


print(sorted(all_names))
print(sorted(neutral_names))
print(sorted(specific_names))
print(sorted(female_difference))
print(sorted(male_difference))
