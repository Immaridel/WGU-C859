the_input = list(map(int, input().strip().split()))
ranges = list(map(int, input().strip().split()))

for i in range(len(the_input)):
    if (the_input[i] >= ranges[0]) and (the_input[i] <= ranges[1]):
        print(the_input[i], end=' ')
        