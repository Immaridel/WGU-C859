with open(input()) as f:
#with open('ParkPhotos.txt') as f:
    raw = f.readlines()
    for i in raw:
        replaced = i.replace('_photo.jpg', '_info.txt').strip()
        print(replaced)
