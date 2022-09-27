"""
https://learn.zybooks.com/zybook/WGUC859v4/chapter/14/section/9

1. read in the name of an input file and read the input file using readlines()
    put contents of the input file into a dictionary where the number of seasons are the keys and TV shows are values
        {'20\n': 'Law & Order\n', '30\n': 'The Simpsons\n', '10\n': 'Will & Grace\n', '14\n': 'Dallas\n', '12\n': 'Murder, She Wrote\n'}
2. sort the dictionary by key (L to G) and output the results to a file named output_keys.txt.
3. If a key associates with multiple values, separate those values by semicolon, then sort the values alphabetically.
4. output #3's results to output_titles.txt
"""

file = input()
#file = "file1.txt"
my_dict = {}
sorted_dict = {}
sorted_list = []
with open(file, 'r') as f:
    lines = f.readlines()

for i in range(0, len(lines), 2):
    key = int(lines[i])
    value = lines[i + 1].strip()
    sorted_list.append(value)
    if key in my_dict:
        my_dict[key] = my_dict[key] + '; ' + value
    else:
        my_dict[key] = value
sorted_list.sort()

for sorted_key in sorted(my_dict):
    sorted_dict[str(sorted_key)] = my_dict[sorted_key]

f2 = open("output_keys.txt", "w")
for key, value in sorted_dict.items():
    f2.write(key + ": " + value + '\n')
f2.close()

f3 = open("output_titles.txt", "w")
for value in sorted_list:
    f3.write(value + '\n')
f3.close()