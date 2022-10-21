filename = 'file_text/learning_python'

with open(filename) as file_object:
    for line in file_object.readlines():
        message = line.replace('Python', 'C').strip()
        print(message)
