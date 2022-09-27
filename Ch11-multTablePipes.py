user_input= '1 2 3,2 4 6,3 6 9'
lines = user_input.strip().split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
print(user_input)
print(lines)
mult_table = [[int(num) for num in line.split()] for line in lines]
print(mult_table)
row_length = len(mult_table[0])  # Gets length of the first row.

for row_index, row in enumerate(mult_table):  # Loops trough each row.
    count = 1  # Sets count
    cell_index = 0  # Sets cell index count
    while count != row_length:  # Checks if end of the row
        print(f'{mult_table[row_index][cell_index]} | ', end='')  # Print
        count += 1  # Count increase
        cell_index += 1  # Count increase
    else:
        print(f'{mult_table[row_index][cell_index]}')  # Print
        count += 1  # Count increase
        cell_index += 1  # Count increase
