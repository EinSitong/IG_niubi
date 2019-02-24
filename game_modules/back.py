import pygame


class Background:
    """背景"""
    
    def __init__(self, screen):
        """初始化背景设置"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/before_background.bmp')
        self.rect = self.image.get_rect()

        # 图片位置设置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def paste(self):
        """粘贴背景"""
        self.screen.blit(self.image, self.rect)


class Cover(Background):
    """初始封面"""
    
    def __init__(self, screen, photo_name):
        """继承背景设置"""
        super().__init__(screen)
        self.image = pygame.image.load(photo_name)
        self.rect = self.image.get_rect()
