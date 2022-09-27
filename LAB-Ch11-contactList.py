'''
A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc. Write a program that first takes in word pairs that consist of a name and a phone number (both strings). That list is followed by a name, and your program should output the phone number associated with that name.

Ex: If the input is:
    Joe 123-5432 Linda 983-4123 Frank 867-5309
    Frank

the output is:
    867-5309
'''
contacts = input().strip().split()
lookup = input().strip()
contact_dict = {(contacts[i]): (contacts[i + 1]) for i in range(0, len(contacts), 2)}

print(contact_dict[lookup])
