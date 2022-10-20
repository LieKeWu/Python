pizzas = ['Pizza hut', "McDonald's", 'KFC', 'Ken']
# for pizza in pizzas:
#     print("I like " + pizza + ' Pizza.')
# print("I really love pizza")

friend_pizzas = pizzas[:]
pizzas.append("New")
friend_pizzas.append("Fnew")

for i in pizzas:
    print(i)

print('\n')

for i in friend_pizzas:
    print(i)
