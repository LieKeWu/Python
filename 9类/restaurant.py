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


# my_restaurant = Restaurant('KKK', 'Chinese Food')
# print("Served people number: ")
# print('\t-', my_restaurant.number_served)
#
# print("Increment people number: 0 ")
# my_restaurant.increment_people(0)
# print('\t-', my_restaurant.number_served)
#
# my_restaurant.set_number_served(22)

# one_restaurant = Restaurant("KFC", "fry")
# one_restaurant.describe_restaurant()
#
# two_restaurant = Restaurant("McDonald's", "fry")
# two_restaurant.describe_restaurant()
#
# three_restaurant = Restaurant("绿茶", "chinese food")
# three_restaurant.describe_restaurant()
