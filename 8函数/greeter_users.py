def greeter_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


users = ['ken', 'jiying', 'di']
greeter_users(users)
