class User():
    def __init__(self, first_name, last_name, age, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.gender = gender
        # 登录尝试属性
        self.login_attempts = 0

    def describe_user(self):
        print("First_name: ", self.first_name.title())
        print('Last_name: ', self.last_name.title())
        print('Gge: ', self.age)
        print('Gender: ', self.gender)

    def greet_user(self):
        print("Hey, " + self.first_name.title() + " nice to meet you!")

    def increment_login_attempts(self, number):
        self.login_attempts += number

    def reset_login_attempts(self):
        self.login_attempts = 0
