"""
stringaling = input()
while (stringaling.lower() != "done") and (stringaling.lower() != "d"):
    print(stringaling[::-1])
    stringaling = input()
"""
phrase = input()
while (phrase.lower() != "d") and (phrase.lower() != "done"):
    print(phrase[::-1])
    phrase = input()