import pygame


class Xiaozhang:
    """王校长"""
    
    def __init__(self, ig_settings, screen):
        """初始化校长设置"""
        
        self.screen = screen
        self.ig_settings = ig_settings
        
        # 图片与位置初始化
        
        self.raw_image = pygame.image.load('images/xiaozhang.png')
        self.image = self.raw_image
        
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # 移动标志
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False
        
    def update(self):
        """校长位置更新"""
        
        # 移动位置确定
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ig_settings.xiaozhang_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ig_settings.xiaozhang_speed_factor
        
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ig_settings.xiaozhang_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ig_settings.xiaozhang_speed_factor
        
        # 移动位置更新
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def center_xiaozhang(self):
        """重置校长位置"""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery
    
    def paste(self):
        """粘贴校长"""
        self.screen.blit(self.image, self.rect)
