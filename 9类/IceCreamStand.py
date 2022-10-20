"""
冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4
而编写的Restaurant类。这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。

"""


class Restaurant():
    """创建一个餐厅的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐厅名字和烹饪类型"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 就餐人数
        self.number_served = 23

    def describe_restaurant(self):
        """输出餐厅名字和烹饪类型"""
        print("\nThe name of this restaurant is: " + self.restaurant_name)
        print("Restaurant-Type: " + self.cuisine_type)

    def open_restaurant(self):
        """显示正在营业"""
        print(self.restaurant_name + " is open.")

    def set_number_served(self, number):
        """设置人数不能比原来的少"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You Can't roll back served date.")

    def increment_people(self, number):
        """增加人数不能为负数"""
        if number >= 0:
            self.number_served += number
        else:
            print("You Can't roll back served date.")


class IceCreamStand(Restaurant):
    """ 冰淇淋小店"""

    def __init__(self, resaurant_name, cuisine_type):
        """
        初始化父类信息
        再初始化冰淇淋店独有属性
        """
        super().__init__(resaurant_name, cuisine_type)

    def show_icecream_menu(self, flavors):
        print("Flavros:")
        self.flavors = flavors
        for flavor in flavors:
            print('\t-', flavor)


my_ice = IceCreamStand('KK', 'IceCream')
IceCreamStand.describe_restaurant(my_ice)
flavros = ['apple', 'banana', 'orange']
my_ice.show_icecream_menu(flavros)
