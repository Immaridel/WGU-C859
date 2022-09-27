user_num = int(input())

if user_num < 11 or user_num > 100:
    print("Input must be 11-100")
    exit()

print(user_num)

while user_num != 11:
    num_split = list(str(user_num))
    if num_split[0] != num_split[1]:
        user_num -= 1
        print(user_num)
    else:
        break
