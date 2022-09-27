format_string = '{name:16}{goals:8}'

print(format_string.format(name='Player Name', goals='Goals'))

print('-' * 24)

print(format_string.format(name='Sadio Mane', goals=22))

print(format_string.format(name='Gabriel Jesus', goals=7))

# Same result, different method.
#
# the name and goals fields have to match
# the expected named in the format call.
print('{name:16}{goals:8}'.format(name='Immaridel', goals=100))
