word = str(input())
pal = list(word)
lap = []


for i in pal:
    if i.isalpha():
        lap.append(i)

crap = lap

for i in range(len(crap)):
    if crap[i-1] != crap[-i]:
        print(f'{word} is not a palindrome')
        exit()

print(f'{word} is a palindrome')
