r = int(input())
g = int(input())
b = int(input())

rgblist = [r, g, b]
smallest = min(rgblist)

r = r - smallest
b = b - smallest
g = g - smallest

print(r, g, b)
