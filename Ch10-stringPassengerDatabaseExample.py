menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS']

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination

    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for destination in passengers:
            print('{} --> {}'.format(destination.title(), passengers[destination]))
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()