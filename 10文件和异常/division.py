print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_name = input("\nFirst number: ")
    if first_name == 'q':
        break

    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_name) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
