class Employee():
    """创建一个雇员的类"""

    def __init__(self, first_name, last_name, annual_salary):
        """
        :param first_name: 接收名字
        :param last_name: 接收姓氏
        :param annual_salary: 接收年薪
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        """默认加薪5000美元"""
        self.annual_salary += salary_raise
        return self.annual_salary
