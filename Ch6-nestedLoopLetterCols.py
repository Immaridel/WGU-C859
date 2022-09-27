num_rows = 2
num_cols = 3

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

# 1A 1B 1C 2A 2B 2C

char1 = int(1)
char2 = 'a'

for x in range(num_rows):
    char2 = 'a'.upper()
    for y in range(num_cols):
         print('{}{}'.format(char1, char2.upper()), end=' ')
         char2 = chr(ord(char2) + 1)
    char1 += 1
print()