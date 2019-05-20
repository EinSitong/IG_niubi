import pygame
import time
import random

from game_modules.buttons import Button
from game_modules.hot_dogs import HotDog
from game_modules.dogfaces import DogFace


# functions for events geted.

def check_mousedown_events(ig_settings, stats, buttons, back_button, windows,
                           mouse_x, mouse_y, hot_dogs, dogfaces, xiaozhang):
    """检测鼠标点击事件"""

    # 开始界面按钮点击判断
    if not stats.game_active and not stats.zgf_sign:

        # 开始按钮判断
        if buttons[0].rect.collidepoint(mouse_x, mouse_y) and buttons[0].valid_flag:
            if stats.game_data["xiaozhang_left"] == 0:
                new_start(stats, ig_settings, hot_dogs, dogfaces, xiaozhang)
            else:
                window_pop("begin", buttons, back_button, windows)

        # 继续按钮判断.
        elif buttons[1].rect.collidepoint(mouse_x, mouse_y) and buttons[1].valid_flag:
            if stats.game_data["xiaozhang_left"] == 0:
                window_pop("continue", buttons, back_button, windows)
            else:
                stats.game_active = True

        # 最高分按钮判断.
        elif buttons[2].rect.collidepoint(mouse_x, mouse_y) and buttons[2].valid_flag:
            stats.zgf_sign = True

        # 退出按钮判断.
        elif buttons[3].rect.collidepoint(mouse_x, mouse_y) and buttons[3].valid_flag:
            stats.game_over = True

    # 非开始界面,返回按钮判断.
    elif stats.game_active or stats.zgf_sign:
        if back_button.rect.collidepoint(mouse_x, mouse_y) and back_button.valid_flag:
            stats.game_active = False
            stats.zgf_sign = False

    # 弹窗界面按钮判断.

    # begin窗口判断.
    if windows["begin"].active:

        # yes按钮判断.
        if windows["begin"].buttons["yes"].rect.collidepoint(mouse_x, mouse_y):
            # 记录旧分数并开始.
            stats.scores.append(stats.game_data["score"])
            stats.scores.sort(reverse=True)
            del stats.scores[-1]
            window_pop("begin", buttons, back_button, windows)
            new_start(stats, ig_settings, hot_dogs, dogfaces, xiaozhang)

        # no按钮判断
        elif windows["begin"].buttons["no"].rect.collidepoint(mouse_x, mouse_y):
            # 继续.
            window_pop("begin", buttons, back_button, windows)
            stats.game_active = True

        # quit按钮判断.
        elif windows["begin"].buttons["quit"].rect.collidepoint(mouse_x, mouse_y):
            # 退出窗口.
            window_pop("begin", buttons, back_button, windows)

    # continue窗口判断.
    if windows["continue"].active:

        # yes按钮判断.
        if windows["continue"].buttons["yes"].rect.collidepoint(mouse_x, mouse_y):
            # 新开始游戏.
            window_pop("continue", buttons, back_button, windows)
            new_start(stats, ig_settings, hot_dogs, dogfaces, xiaozhang)

        # no或quit按钮判断
        elif windows["continue"].buttons["no"].rect.collidepoint(mouse_x, mouse_y) or \
                windows["continue"].buttons["quit"].rect.collidepoint(mouse_x, mouse_y):
            # 退出窗口.
            window_pop("continue", buttons, back_button, windows)


def check_keydowm_events(event, ig_settings, stats, xiaozhang, hot_dogs):
    """一个键为一个事件，检查一个按键事件"""

    if event.key == pygame.K_ESCAPE:
        if stats.game_active or stats.zgf_sign:
            stats.game_active = False
            stats.zgf_sign = False
        else:
            stats.game_over = True

    elif event.key == pygame.K_d:
        xiaozhang.moving_right = True
        xiaozhang.image = xiaozhang.raw_image
        stats.dogflagxy = True
        stats.dogflagzf = True

    elif event.key == pygame.K_a:
        xiaozhang.moving_left = True
        xiaozhang.image = pygame.transform.flip(
            xiaozhang.raw_image, True, False)
        stats.dogflagxy = True
        stats.dogflagzf = False

    elif event.key == pygame.K_w:
        xiaozhang.moving_up = True
        xiaozhang.image = pygame.transform.rotate(xiaozhang.raw_image, 90)
        stats.dogflagxy = False
        stats.dogflagzf = True

    elif event.key == pygame.K_s:
        xiaozhang.moving_down = True
        xiaozhang.image = pygame.transform.rotate(xiaozhang.raw_image, -90)
        stats.dogflagxy = False
        stats.dogflagzf = False

    elif event.key == pygame.K_SPACE:
        shoot(ig_settings, stats, hot_dogs, xiaozhang)


def check_keyup_events(event, xiaozhang):
    """检测按键抬起事件"""
    if event.key == pygame.K_d:
        xiaozhang.moving_right = False

    elif event.key == pygame.K_a:
        xiaozhang.moving_left = False

    elif event.key == pygame.K_w:
        xiaozhang.moving_up = False

    elif event.key == pygame.K_s:
        xiaozhang.moving_down = False


def new_start(stats, ig_settings, hot_dogs, dogfaces, xiaozhang):
    """开始新游戏"""
    stats.reset_stats()
    ig_settings.initialize_dynamic_settings()
    hot_dogs.empty()
    dogfaces.empty()
    xiaozhang.center_xiaozhang()
    stats.game_active = True


def window_pop(window_name, buttons, back_button, windows):
    """弹出/退出指定窗口"""

    # 使外部按钮无效或有效.
    for button in buttons:
        button.valid_flag = not button.valid_flag
    back_button.valid_flag = not back_button.valid_flag

    # 弹窗或退出窗口.
    windows[window_name].active = not windows[window_name].active


# 输入检查合并
def check_events(ig_settings, stats, buttons, back_button, windows,
                 xiaozhang, hot_dogs, dogfaces, clocks):
    """检测输入事件"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            stats.game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mousedown_events(ig_settings, stats, buttons, back_button, windows,
                                   mouse_x, mouse_y, hot_dogs, dogfaces, xiaozhang)

        elif event.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(True)
            clocks.append(time.clock())

        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(
                event, ig_settings, stats, xiaozhang, hot_dogs
            )

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, xiaozhang)


# functions for inside events.

def check_collisions(ig_settings, stats, xiaozhang, hot_dogs, dogfaces):
    """检测单位碰撞事件"""

    # 热狗与小兵碰撞
    kill = pygame.sprite.groupcollide(hot_dogs, dogfaces, True, True)

    # 记录分数
    if kill:
        for dogfaces in kill.values():
            stats.game_data["score"] += len(dogfaces) * \
                ig_settings.dogface_points
            stats.game_data["score"] = int(round(stats.game_data["score"],
                                                 -1))

    # 小兵与校长碰撞
    if pygame.sprite.spritecollideany(xiaozhang, dogfaces):

        stats.game_data["xiaozhang_left"] -= 1

        if stats.game_data["xiaozhang_left"] == 0:

            # 记录旧分数
            stats.scores.append(stats.game_data["score"])
            stats.scores.sort(reverse=True)
            del stats.scores[-1]

            # 结束游戏并打印
            stats.game_active = False
            print("王校长给热狗噎死了")

        else:
            print("王校长给热狗噎到了")
            time.sleep(0.5)
            dogfaces.empty()
            hot_dogs.empty()
            xiaozhang.center_xiaozhang()


def check_game_schedule(ig_settings, stats, screen, hot_dogs, dogfaces):
    """检测游戏进度及小兵刷新与进度提升"""

    if len(dogfaces) == 0:

        # 进度提升
        stats.game_data["round_times"] += 1
        hot_dogs.empty()
        ig_settings.increase_speed()

        # 小兵创建

        # 一大波小兵
        if stats.game_data["round_times"] % 5 == 0:

            ig_settings.dogface_number += 1
            ig_settings.flee_number += 1

            for i in range(ig_settings.flee_number):
                create_flee(
                    ig_settings, screen, dogfaces,
                    random.choice((True, False)),
                    random.choice((True, False))
                )

        # 常规创建
        else:
            for i in range(ig_settings.dogface_number):
                create_dogface(
                    ig_settings, screen, dogfaces,
                    random.choice((True, False)),
                    random.choice((True, False))
                )


# 内部检查合并
def check_inside_events(ig_settings, stats, screen,
                        xiaozhang, hot_dogs, dogfaces, clocks):
    """检测内部事件"""

    # 鼠标隐藏
    interval = time.clock() - clocks[-1]
    if interval >= 3:
        pygame.mouse.set_visible(False)

    # 内部事件检查
    check_game_schedule(ig_settings, stats, screen, hot_dogs, dogfaces)
    check_collisions(ig_settings, stats, xiaozhang, hot_dogs, dogfaces)


# functions for screen update

def update_coverscreen(cover, buttons):
    """更新封面"""

    cover.paste()
    for button in buttons:
        button.paste()

    pygame.display.flip()


def update_backscreen(screen, stats, background, xiaozhang,
                      hot_dogs, dogfaces, back_button):
    """更新背景"""

    # 背景及界面元素粘贴
    background.paste()
    print_score(screen, stats.scores[0], 0, 600,
                font_size=48, font_color=(240, 60, 0))
    print_score(screen, stats.game_data["score"], 50, 600)
    print_score(
        screen, stats.game_data["round_times"], 0, 1000, 48, (64, 16, 8))
    paste_life(screen, stats, xiaozhang)

    # 游戏按钮粘贴.
    back_button.paste()

    # 游戏对象刷新
    xiaozhang.paste()
    hot_dogs.draw(screen)
    dogfaces.draw(screen)

    pygame.display.flip()


def update_secondcover(screen, stats, second_cover, back_button):
    """更新最高分背景"""

    # 背景及其元素粘贴
    second_cover.paste()
    back_button.paste()

    # 分数粘贴
    top, centerx = 70, 900
    for score in stats.scores:
        print_score(screen, score, top, centerx)
        top += 50

    pygame.display.flip()


def print_score(screen, score, top, centerx,
                font_size=32, font_color=(230, 220, 180)):
    """打印分数"""

    # 字体与位置设置
    font = pygame.font.SysFont('SimHei', font_size)
    score_str = "{:,}".format(score)
    image = font.render(score_str, True, font_color)
    image_rect = image.get_rect()
    image_rect.top, image_rect.centerx = top, centerx

    # 粘贴在屏幕
    screen.blit(image, image_rect)


def paste_life(screen, stats, xiaozhang):
    """粘贴生命值"""
    image = pygame.transform.scale(xiaozhang.raw_image, (50, 50))
    image_rect = image.get_rect()
    for i in range(stats.game_data["xiaozhang_left"]):
        screen.blit(image, image_rect)
        image_rect.left += 60


# function of buttons
def create_buttons(ig_settings, screen, buttons):
    """创建按钮"""
    centerx, centery = 600, 490
    for msg in ("开始", "继续", "最高分", "退出"):
        button = Button(ig_settings, screen, "images/button.bmp", msg)
        button.rect.center = (centerx, centery)
        button.image_equal_rect()
        buttons.append(button)
        centery += 70


# function of hot_dog
def shoot(ig_settings, stats, hot_dogs, xiaozhang):
    """吐出热狗"""

    if stats.dogflagxy and stats.dogflagzf:
        hot_dog = HotDog(ig_settings, stats, xiaozhang, hot_dogs)
        hot_dog.centerx += 35
        hot_dogs.add(hot_dog)

    elif stats.dogflagxy:
        hot_dog = HotDog(ig_settings, stats, xiaozhang, hot_dogs)
        hot_dog.centerx -= 35
        hot_dog.image = pygame.transform.flip(hot_dog.image, True, False)
        hot_dogs.add(hot_dog)

    elif stats.dogflagzf:
        hot_dog = HotDog(ig_settings, stats, xiaozhang, hot_dogs)
        hot_dog.centery -= 35
        hot_dog.image = pygame.transform.rotate(hot_dog.image, 90)
        hot_dogs.add(hot_dog)

    else:
        hot_dog = HotDog(ig_settings, stats, xiaozhang, hot_dogs)
        hot_dog.centery += 35
        hot_dog.image = pygame.transform.rotate(hot_dog.image, -90)
        hot_dogs.add(hot_dog)


# functions of dogfaces

def create_dogface(ig_settings, screen, dogfaces, dogface_rb, dogface_fx):
    """在宽/高上随机创建小兵"""

    # 创建
    dogface = DogFace(ig_settings, screen)

    # 生成位置
    if dogface_rb:
        dogface.r = random.uniform(dogface.rect.width - 1, 1199)
        dogface.ymoving_right = True
        if not dogface_fx:
            dogface.b = 800
            dogface.ymoving_right = False
    else:
        dogface.b = random.uniform(dogface.rect.height - 1, 799)
        dogface.xmoving_right = True
        if not dogface_fx:
            dogface.r = 1200
            dogface.xmoving_right = False

    # 加入
    dogfaces.add(dogface)


def create_flee(ig_settings, screen, dogfaces, flee_rb, flee_fx):
    """创建n行/列小兵"""

    # 计算数目
    dogface = DogFace(ig_settings, screen)
    if flee_rb:
        dogface_cd = dogface.rect.width
        screen_cd = ig_settings.screen_width
    else:
        dogface_cd = dogface.rect.height
        screen_cd = ig_settings.screen_height
    xnumber_dogfaces = screen_cd // (3 * dogface_cd)
    dogface_blank = (screen_cd - 3 * dogface_cd * xnumber_dogfaces) // 2

    # 创建几行/列小兵并确定位置
    for dogface_n in range(xnumber_dogfaces):

        dogface = DogFace(ig_settings, screen)

        if flee_rb:
            dogface.r += dogface_blank + 2 * dogface_cd * dogface_n
            dogface.ymoving_right = True
            if not flee_fx:
                dogface.b = 800
                dogface.ymoving_right = False
        else:
            dogface.b += dogface_blank + 2 * dogface_cd * dogface_n
            dogface.xmoving_right = True
            if not flee_fx:
                dogface.r = 1200
                dogface.xmoving_right = False

        dogfaces.add(dogface)
