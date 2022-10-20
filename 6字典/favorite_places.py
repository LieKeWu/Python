favorite_places = {
    'ken': ['Japan', 'USA', 'UK'],
    'Jiying': ['France', 'ice land'],
    'di': ['China']
}

for name, places in favorite_places.items():
    print(name.title() + " want to go:")
    for place in places:
        print("\t" + place)
