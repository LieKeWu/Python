rivers = {
    'niel': 'egypt',
    'Changjiang': 'china',
    'Suez': 'france'
}

for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + ".")

for river in rivers.keys():
    print(river)
    print('\t' + rivers[river])
