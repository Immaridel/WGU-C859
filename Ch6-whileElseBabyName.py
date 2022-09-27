import edit_distance
#can't run because we don't have that module...

#A few legal, acceptable Danish names
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn',
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne',
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia',
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne',
    'Dorte'
]

user_name = input('Enter desired name:\n')
if user_name in legal_names:
    print('{} is an acceptable Danish name. Congratulations.'.format(user_name))
else:
    print('{} is not acceptable.'.format(user_name))
    for name in legal_names:
        if edit_distance.distance(name, user_name)  < 2:
            print('You might consider: {},'.format(name), end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')