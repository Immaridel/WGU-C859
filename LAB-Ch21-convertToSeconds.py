hours = int(input())
mins = int(input())
secs = int(input())

h2s = (hours * 60) * 60
m2s = (mins * 60)

print('Seconds: {}'.format(h2s + m2s + secs))
