import pygame
import random
from pygame.sprite import Sprite


class DogFace(Sprite):
    """小兵"""

    def __init__(self, ig_settings, screen):
        """初始化小兵设置"""

        super().__init__()
        self.screen = screen
        self.ig_settings = ig_settings

        # 小兵图像及位置初始化
        self.image = pygame.image.load("images/dogface.png")
        self.rect = self.image.get_rect()
        self.r = float(self.rect.right)
        self.b = float(self.rect.bottom)

        # 移动方向标记
        self.xmoving_right = random.choice((True, False))
        self.ymoving_right = random.choice((True, False))

    def update(self):
        """更新小兵位置"""

        # 横向移动
        if self.xmoving_right:
            self.r += self.ig_settings.dogface_speed
        else:
            self.r -= self.ig_settings.dogface_speed
        if self.r <= self.rect.width or \
                self.r >= self.ig_settings.screen_width:
            self.xmoving_right = not self.xmoving_right

        # 纵向移动
        if self.ymoving_right:
            self.b += self.ig_settings.dogface_speed
        else:
            self.b -= self.ig_settings.dogface_speed
        if self.b <= self.rect.height or \
                self.b >= self.ig_settings.screen_height:
            self.ymoving_right = not self.ymoving_right

        # 位置更新
        self.rect.right = self.r
        self.rect.bottom = self.b
