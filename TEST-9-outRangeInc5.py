num1 = int(input())
num2 = int(input())

if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    while num1 <= num2:
        print(num1, end=" ")
        num1 += 5
    print()