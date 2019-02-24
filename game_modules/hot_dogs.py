import pygame
from pygame.sprite import Sprite


class HotDog(Sprite):
    """热狗子弹"""
    
    def __init__(self, ig_settings, stats, xiaozhang, hot_dogs):
        """初始化热狗设置"""

        super().__init__()
        self.ig_settings = ig_settings
        self.hot_dogs = hot_dogs

        # 图像位置初始化
        self.image = pygame.image.load('images/hot_dog.png')
        self.rect = self.image.get_rect()
        self.centerx = float(xiaozhang.rect.centerx)
        self.centery = float(xiaozhang.rect.centery)

        # 热狗方向标记
        self.flag_xy = stats.dogflagxy
        self.flag_zf = stats.dogflagzf

    def update(self):
        """更新热狗位置"""

        # 移动位置确定

        if self.flag_xy and self.flag_zf:
            if self.rect.left >= 1200:
                self.hot_dogs.remove(self)
            else:
                self.centerx += self.ig_settings.hot_dog_speed_factor

        elif self.flag_xy:
            if self.rect.right <= 0:
                self.hot_dogs.remove(self)
            else:
                self.centerx -= self.ig_settings.hot_dog_speed_factor

        elif self.flag_zf:
            if self.rect.bottom <= 0:
                self.hot_dogs.remove(self)
            else:
                self.centery -= self.ig_settings.hot_dog_speed_factor

        else:
            if self.rect.top >= 800:
                self.hot_dogs.remove(self)
            else:
                self.centery += self.ig_settings.hot_dog_speed_factor

        # 移动位置更新
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
