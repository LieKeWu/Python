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


my_admin = Privilegs()
my_admin.show_privileges()
