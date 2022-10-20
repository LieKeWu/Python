def make_sandwich(*toppings):
    """制作三明治"""
    print('\n您制作的三明治清单如下:')
    for topping in toppings:
        print('\t- ' + topping)


make_sandwich('apple')
make_sandwich('banana', 'watermelon')
make_sandwich('apple', 'pear', 'egg')
