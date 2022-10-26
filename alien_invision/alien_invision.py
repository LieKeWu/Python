import sys
import pygame
from setting import Settings


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()  # 初始化背景设置
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_hight))  # 设置宽高
    pygame.display.set_caption("Alien Invision")  # 设置应用标题

    # 开启游戏住循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击关闭按钮，退出游戏
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(ai_setting.bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
