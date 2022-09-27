synonyms = {}  # Define dictionary

user = input()
letter = input()

with open(user + '.txt', 'r') as f:
    lines = f.readlines()
    for word in lines:
        key = word[0]
        words = word.split()
        synonyms[key] = words

if letter in synonyms:
    for i in synonyms[letter]:
        print(i)
else:
    print(f'No synonyms for {user} begin with {letter}.')
