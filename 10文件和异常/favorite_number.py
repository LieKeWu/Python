import json

filename = 'favorite.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('What is Your favorite number?')
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I Know your favorite number! It's " + str(number) + ' .')
