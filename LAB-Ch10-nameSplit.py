'''
steven
russell
cameron
'''

fullname = input().strip().split(' ')

lastname = fullname[-1]
fullname.pop(-1)
print('{}, '.format(lastname.title()), end="")

for names in fullname:
    print('{}.'.format(names[0].upper()), end="")
print()
