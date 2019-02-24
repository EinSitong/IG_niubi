import pygame.font


class Button:
    """游戏按钮"""

    def __init__(self, ig_settings, screen, photo_name, msg):
        """初始化按钮设置"""
        
        self.ig_settings = ig_settings
        self.screen = screen

        # 有效标志.
        self.valid_flag = True
        
        # 按钮图片及其位置设置
        self.image = pygame.image.load(photo_name)
        self.rect = self.image.get_rect()
        
        # 文字设置
        self.font = pygame.font.SysFont('SimHei', 32)
        self.msg_image = self.font.render(msg, True, (230, 220, 180))
        self.msg_image_rect = self.msg_image.get_rect()

    def paste(self):
        """粘贴"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def image_equal_rect(self):
        """将文字中心与按钮中心对正"""
        self.msg_image_rect.center = self.rect.center
