class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车历程的信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

# 
# my_new_car = Car('Tesla', 'model3', 2024)
# print(my_new_car.get_describe_name())
# my_new_car.read_odometer()
#
# # print("\n试驾后：")
# # # my_new_car.odometer_reading = 23
# # my_new_car.update_odometer(24)
# # my_new_car.read_odometer()
# print('\nincrement 23500 miles:')
# my_new_car.increment_odometer(23500)
# my_new_car.read_odometer()
# print('\nincrement 23 miles:')
# my_new_car.increment_odometer(23)
# my_new_car.read_odometer()
#
# print('\nincrement -1 miles:')
# my_new_car.increment_odometer(-1)
# my_new_car.read_odometer()
