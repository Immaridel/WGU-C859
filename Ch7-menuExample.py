def print_menu():
    print("Today's Menu:")
    print('   1) Gumbo')
    print('   2) Jambalaya')
    print('   3) Quit\n')

quit_program = False

while not quit_program :
    print_menu()
    choice = int(input('Enter choice: '))
    if choice == 3 :
        print('Goodbye')
        quit_program = True
    else :
        print('Order: ')
        if choice == 1 :
            print('Gumbo')
        elif choice == 2 :
            print('Jambalaya')
        print()