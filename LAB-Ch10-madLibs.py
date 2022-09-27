libput = input().strip().split(' ')
while libput[0].lower() != 'quit':
    if len(libput) < 2:
        print('Not enough arguments.')
        exit()
    else:
        print('Eating {} {} a day keeps the doctor away.'.format(libput[1], libput[0]))
        libput = input().strip().split(' ')
