import json


def show_favorite_nubmer():
    filename = 'favorite.json'
    with open(filename) as f_obj:
        number = json.load(f_obj)
        print("I know your favorite number! It's " + str(number) + ".")


show_favorite_nubmer()
