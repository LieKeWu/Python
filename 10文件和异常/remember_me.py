import json


# 如果用户已经存在，直接问候,否则加入文件。

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return name


def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    if username:
        correct = input('Are you ' + username + " ? (Y/N)")
        if correct == 'y':
            print('Welcom back, ' + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you com back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you com back, " + username + "!")


greet_user()
