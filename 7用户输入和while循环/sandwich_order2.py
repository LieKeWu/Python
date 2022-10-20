sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'KFC', "McDonald's",
                   'Subway']

finished_orders = []

print('pastrami is empty.')

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    make = sandwich_orders.pop()
    finished_orders.append(make)
print('\nfinished_order:')
for finished_order in finished_orders:
    print('\t' + finished_order)
