#seconds = int(input())
seconds = 4000

hours = int(seconds // 60) // 60
mins = int(seconds // 60) % 60
secs = int(seconds % 60)

print('Hours: {}'.format(hours))
print('Minutes: {}'.format(mins))
print('Seconds: {}'.format(secs))