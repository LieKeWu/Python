person1 = {
    'first_name': 'Liken',
    'last_name': 'Wu',
    'age': 25,
    'city': 'Hangzhou'
}
person2 = {
    'first_name': 'Di',
    'last_name': 'Wu',
    'age': 14,
    'city': 'Hangzhou'
}
person3 = {
    'first_name': 'Jiying',
    'last_name': 'Zheng',
    'age': 23,
    'city': 'Hangzhou'
}

peoples = [person3, person2, person1]
for people in peoples:
    print(people['first_name'] + "" + people['last_name'] + ", " + str(
        people['age']) + ', ' + people['city'])
