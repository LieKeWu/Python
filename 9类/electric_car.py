from car import Car


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条电瓶容量消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self, car_model):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car(" + car_model + ") can go approximately " + str(
            range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        """提升电量方法"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动车的独到之处"""

    def __init__(self, make, model, year):
        """
        初始化父类信息
        再初始化电动汽车独有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")


# my_gascar = Car('audi', 'Q3', 2018)
# print(my_gascar.get_describe_name())
# my_gascar.fill_gas_tank()
#
# my_tesla = Electric('tesla', 'model s', 2016)
# print(my_tesla.get_describe_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range(my_tesla.model)
#
# print('提升Tesla 电池后：')
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range(my_tesla.model)
