par = int(input())
strokes = int(input())

if par < 3 or par > 5:
    print('Error')
    exit()
else:
    if par - strokes == 2:
        print('Eagle')
        exit()
    elif par - strokes == 1:
        print('Birdie')
        exit()
    elif par - strokes == 0:
        print('Par')
        exit()
    elif par - strokes == -1:
        print('Bogey')