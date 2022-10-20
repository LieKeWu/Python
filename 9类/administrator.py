"""
“管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
添加一个名为privileges(特权)的属性
用于存储一个由字符串
（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。”
"""
from user import User


class Admin(User):
    """创建一个管理员的类,继承User类"""

    def __init__(self, first_name, last_name, age, gender):
        """
        初始化父类信息
        再初始化管理员独有信息
        """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]

    def show_privileges(self):
        print("\nYour are administrator\nAdmin's privileges are:")
        for i in self.privileges:
            print('\t-' + i)


class Privilegs():
    """创建一个权限的类"""

    def __init__(self):
        """初始化类"""
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]

    def show_privileges(self):
        # 显示权限
        print("\nYour are administrator\nAdmin's privileges are:")
        for i in self.privileges:
            print('\t-' + i)

#
# admin = Admin('liken', 'wu', 25, 'male')
# admin.greet_user()
# admin.describe_user()
# admin.show_privileges()
