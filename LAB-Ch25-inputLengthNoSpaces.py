string = input()
count = 0

for i in string:
    if (i != "!") and (i != ".") and (i != ",") and (not i.isspace()):
        count += 1

print(count)