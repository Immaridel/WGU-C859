"""
"Simplicity is the key to brilliance." - Bruce Lee
sha224
"""
# FIXME: Import sha224 also
from hashlib import md5, sha1, sha224

text = input("Enter text to hash ('q' to quit): ")

# Add sha224 to prompt
algorithm = input('\nEnter algorithm (md5/sha1/sha224): ')
if algorithm == 'md5':
    output = md5(text.encode('utf-8'))
elif algorithm == 'sha224':
    output = sha224(text.encode('utf-8'))
elif algorithm == 'sha1':
    output = sha1(text.encode('utf-8'))
    # FIXME: Add check for sha224 above
else:
    output = 'Invalid algorithm selection'

print('\nHash value:', output.hexdigest())

