num_insects = int(input()) # Must be >= 1

while (num_insects >= 1) and (num_insects <= 100):
    print('{} '.format(num_insects), end='')
    num_insects = num_insects * 2