xiugou = {
    'type': 'Dog',
    'master_name': 'Ken'
}

miaomiao = {
    'type': 'Cat',
    'master_name': 'Ying'
}

pets = [xiugou, miaomiao]
for pet in pets:
    print(pet['master_name'] + " Have a " + pet['type'] + ".")
