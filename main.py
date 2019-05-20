import sys
import pygame
import csv
from pygame.sprite import Group

from game_modules.settings import Settings
from game_modules.game_stats import GameStats
from game_modules.back import Background, Cover
from game_modules.xiaozhang import Xiaozhang
from game_modules.buttons import Button
from game_modules.window import Window
import game_modules.game_functions as gf


def run_game():
    """定义游戏"""
    # 初始化
    pygame.init()

    # 设置与数据对象创建
    ig_settings = Settings()
    stats = GameStats(ig_settings)

    # 屏幕创建
    screen = pygame.display.set_mode(
        (ig_settings.screen_width, ig_settings.screen_height),
        pygame.FULLSCREEN)
    pygame.display.set_caption("IG牛逼")

    # 背景创建
    background = Background(screen)
    cover = Cover(screen, 'images/cover.bmp')
    second_cover = Cover(screen, 'images/second_cover.bmp')

    # 按钮创建
    buttons = []
    gf.create_buttons(ig_settings, screen, buttons)
    back_button = Button(ig_settings, screen, 'images/button2.png', '')
    back_button.rect.center = (1180, 20)
    back_button.image_equal_rect()

    # 弹窗创建.
    windows = dict()
    windows["begin"] = Window(ig_settings, screen, msg="You old game is still exist, "
                              "are you sure to start a new game?")
    windows["continue"] = Window(ig_settings, screen, msg="You game is over, "
                                 "do you want to start a new game?")

    # 游戏对象创建
    xiaozhang = Xiaozhang(ig_settings, screen)
    hot_dogs, dogfaces = Group(), Group()

    # 记时
    clocks = []

    # 游戏循环
    while True:

        # 检查输入事件
        gf.check_events(ig_settings, stats, buttons, back_button, windows,
                        xiaozhang, hot_dogs, dogfaces, clocks)

        # 游戏更新

        if stats.game_active:

            # 游戏对象更新
            xiaozhang.update()
            hot_dogs.update()
            dogfaces.update()

            # 内部事件检查与更新
            gf.check_inside_events(ig_settings, stats, screen,
                                   xiaozhang, hot_dogs, dogfaces, clocks)

            # 刷新游戏屏幕
            gf.update_backscreen(screen, stats, background, xiaozhang,
                                 hot_dogs, dogfaces, back_button)

        else:

            # 刷新最高分界面
            if stats.zgf_sign:
                gf.update_secondcover(screen, stats, second_cover, back_button)

            # 刷新封面
            else:
                gf.update_coverscreen(cover, buttons)

        # 弹窗更新
        for window in windows.values():
            if window.active:
                window.paste()
        pygame.display.flip()

        # 游戏结束检测
        if stats.game_over:

            # 保存分数
            with open("game_data/scores.txt", 'w') as file_object:
                for score in stats.scores:
                    file_object.write(str(score) + '\n')

            # 保存游戏数据
            with open("game_data/game_data.csv", 'w') as f:
                headers = [key for key in stats.game_data]
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerow(stats.game_data)

            # 保存动态设置

            sys.exit()


# 开始游戏
run_game()
