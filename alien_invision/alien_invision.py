import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()  # 初始化背景设置
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_hight))  # 设置宽高
    pygame.display.set_caption("Alien Invision")  # 设置应用标题

    # 创造一艘飞船
    ship = Ship(screen)

    # 开启游戏住循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events()
        # 每次循环都重绘屏幕
        gf.update_screen()


run_game()
