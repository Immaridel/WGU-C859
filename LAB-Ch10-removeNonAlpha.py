string = input().strip()
new_string = ''.join(character for character in string if character.isalpha())
print(new_string)
