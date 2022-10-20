"""一个用于表示汽车的类"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """
        初始化描述汽车的属性
        :param make:厂商
        :param model: 型号
        :param year: 年份
        """
        self.make = make
        self.model = model
        self.year = year
        # 出厂里程数
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def reading_odometer(self):
        """打印一条消息，指出汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """更新里程表数值，禁止数值回拨"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """插入数值"""
        self.odometer_reading += miles


