word = input('What word would you like to test?: ').strip().lower()
num_guesses = (len(word) + 5)

hidden_word = '-' * len(word)

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input('Enter a character (guess #{}): '.format(guess))

    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)

        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            # Find the position of the next occurrence
            position = word.find(user_input, position + 1)
            # Rebuild the hidden word string
            hidden_word = hidden_word[:position] + user_input + hidden_word[position + 1:]
        guess += 1

if not '-' in hidden_word:
    print('Winner!', end=' ')
else:
    print('Loser!', end=' ')

print('The word was {}.'.format(word))