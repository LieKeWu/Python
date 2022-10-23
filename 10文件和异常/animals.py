filename = 'file_text/dogs.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
print(contents)

filename = 'file_text/cats.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
print(contents)
