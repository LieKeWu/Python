sandwich_orders = ['Subway', 'KFC', "McDonald's"]

finished_sandwiches = []

while sandwich_orders:
    make_sandwich = sandwich_orders.pop()
    print('I made your ' + make_sandwich + ' sandwich.')
    finished_sandwiches.append(make_sandwich)

print('\nall done:')
for done_sandwich in finished_sandwiches:
    print('\t' + done_sandwich)
