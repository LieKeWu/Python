filename = 'alice.txt'

try:
    with open(filename) as f_ob:
        contents = f_ob
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
