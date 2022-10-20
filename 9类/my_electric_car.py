from car import ElectricCar

my_tesla = ElectricCar('Tesla', 'model3', 2022)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
