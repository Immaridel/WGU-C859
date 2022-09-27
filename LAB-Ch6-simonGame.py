user_score = 0
simon_pattern = input()
user_pattern  = input()

if range(len(user_pattern)) != range(len(simon_pattern)):
    print("Entries must be the same length.")
    exit()

for i in range(len(user_pattern)):
    if user_pattern[i] != simon_pattern[i]:
        break
    else:
        user_score += 1

print('User score:', user_score)