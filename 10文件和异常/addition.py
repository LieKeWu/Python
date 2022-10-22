while True:
    try:
        first_number = int(input("\nPlease enter first number: "))
        second_number = int(input("Please enter second number: "))
    except ValueError:
        print("Please enter number, string can't to be calculated!")
    else:
        sum = first_number + second_number
        print(str(first_number) + " + " + str(second_number) +
              " = " + str(sum))
