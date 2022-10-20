import random
from random import randint


class Die():
    """模拟骰子"""

    def __init__(self, number, sides=6):
        """
        :param number: 投掷次数
        :param sides:  X面体骰子
        """
        self.sides = sides
        self.number = number

    def roll_die(self):
        print('\n' + str(self.sides) + '面体骰子, 投掷次数为' + str(
            self.number) + "次。")
        print("\t开始投掷！")

        #投掷次数循环
        for i in range(self.number):
            x = randint(1, self.sides)

        print('\t结果为:', x)


my_dice = Die(1, 6)
my_dice.roll_die()
my_dice = Die(10, 6)
my_dice.roll_die()
my_dice = Die(10, 10)
my_dice.roll_die()
my_dice = Die(10, 20)
my_dice.roll_die()
