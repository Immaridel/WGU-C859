user_input = input('Enter phone number:\n')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a'.lower() <= character.lower() <= 'c'.lower()):
        phone_number += '2'
    elif ('d'.lower() <= character.lower() <= 'f'.lower()):
        phone_number += '3'
    elif ('g'.lower() <= character.lower() <= 'i'.lower()):
        phone_number += '4'
    elif ('j'.lower() <= character.lower() <= 'l'.lower()):
        phone_number += '5'
    elif ('m'.lower() <= character.lower() <= 'o'.lower()):
        phone_number += '6'
    elif ('p'.lower() <= character.lower() <= 's'.lower()):
        phone_number += '7'
    elif ('t'.lower() <= character.lower() <= 'v'.lower()):
        phone_number += '8'
    elif ('w'.lower() <= character.lower() <= 'z'.lower()):
        phone_number += '9'
    #FIXME: Add remaining elif branches
    else:
        phone_number += '?'

print('Numbers only: {}'.format(phone_number))
