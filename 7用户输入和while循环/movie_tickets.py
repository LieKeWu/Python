age = "\nPlease enter your age:"
age += "\nAnd I'll tell your ticket's price."

while True:
    age = int(input(age))
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age == 10086:
        print('quit')
        break
    else:
        price = 15

    print('Your age is', age, ',pay $', price, '.')
