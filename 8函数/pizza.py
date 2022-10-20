# def make_pizza(*toppings):  # *空元组
#     # 打印顾客所有的配料
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ---------------------------------------------------------------

# def make_pizza(*toppings):
#     """概述要制作的披萨"""
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# #---------------------------------------------------------------

def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print('\nMaking a ' + str(size) +
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

#
# make_pizza(6, 'pepperoni')
# make_pizza(13, 'mushrooms', 'green peppers', 'extra cheese')
