m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('{}'.format(m3[i][j]), end=' ')
    print()  # Print single newline
