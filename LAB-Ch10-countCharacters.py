the_string = input().strip().split(' ')
search = the_string[0]
the_string.pop(0)

times = len(the_string)
counter = int()
total = int()

for i in range(0, len(the_string)):
    counter = the_string[i].count(search)
    total += counter
print(total)
