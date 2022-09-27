the_input = input().strip().split()
caw = [int(i) for i in the_input]
nums = []

for i in caw:
    if i >= 0:
        nums.append(i)

nums.sort()
str_it = [str(i) for i in nums]
print(' '.join(str_it), end=' ')
