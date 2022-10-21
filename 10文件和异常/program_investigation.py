filename = 'programming_reasons.txt'

while True:
    reasons = input("Please input the reason why you like programming:")
    with open(filename, 'a') as file_object:
        file_object.write(reasons + '\n')
