toppings = "\nPlease enter  toppings with your pizza:"
toppings += "\nEnter 'quit' finish order."

while True:
    message = input(toppings)
    if message == "quit":
        break
    print("you add topping is:" + message)

print("Thank your ordered!")
