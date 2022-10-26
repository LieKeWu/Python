import json


# 如果用户已经存在，直接问候,否则加入文件。

def greet_user():
    """问候用户，并指出其姓名"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            name = json.load(f_obj)
    except FileNotFoundError:
        name = input("What is your name?")
        with open(filename, 'w') as f_obj:
            json.dump(name, f_obj)
            print("We'll remember you when you com back, " + name + "!")
    else:
        print('Welcome ' + name + "!")

greet_user()
