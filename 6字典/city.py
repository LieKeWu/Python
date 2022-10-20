cities = {
    'Hangzhou': {
        'country': 'China',
        'population': 12000000,
        'fact': 'west lake'
    },
    'Paris': {
        'country': 'France',
        'population': 2160000,
        'fact': 'Eiffel Tower'
    },
    'Kyoto': {
        'country': 'Japan',
        'population': 1475000,
        'fact': 'Daitokuji'
    }
}

for city, city_info in cities.items():
    print(city.upper() + "'s info: ")
    for x, x2 in city_info.items():
        print('\t' + x + ":" + str(x2))
    print()
