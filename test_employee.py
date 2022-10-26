import unittest
from Employee import Employee


class TestEmployeeCase(unittest.TestCase):
    """测试雇员类"""

    def test_give_default_raise(self):
        """用来测试默认加薪5000"""
        my_employee = Employee("Liken", "Wu", 10000)
        salary_raise = my_employee.give_raise()
        self.assertEqual(salary_raise, 15000)

    def test_give_gustom_raise(self):
        """用来测试自定义加薪数额"""
        my_employee = Employee("Liken", "Wu", 10000)
        salary_raise = my_employee.give_raise(4000)
        self.assertEqual(salary_raise, 14000)


unittest.main
