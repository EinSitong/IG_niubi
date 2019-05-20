import pygame
from game_modules.buttons import Button


class Window:
    """窗口"""

    def __init__(self, ig_settings, screen, msg):
        """初始化窗口信息."""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/window.png")
        self.rect = self.image.get_rect()

        # 弹窗与否.
        self.active = False

        # 图片位置设置.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 文字设置.
        self.font = pygame.font.SysFont('SimHei', 16)
        self.msg_image = self.font.render(msg, True, (230, 220, 180))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.top = self.rect.top + self.rect.height // 4
        self.msg_image_rect.centerx = self.screen_rect.centerx

        # 按钮设置.
        self.buttons = dict()

        self.buttons["quit"] = Button(
            ig_settings, screen, "images/win_quit.png", '')
        self.buttons["quit"].rect.topright = self.rect.topright
        self.buttons["quit"].image_equal_rect()

        self.buttons["yes"] = Button(
            ig_settings, screen, "images/win_yes.png", "是")
        self.buttons["yes"].rect.top = self.rect.top + 157
        self.buttons["yes"].rect.left = self.rect.left + 77
        self.buttons["yes"].image_equal_rect()

        self.buttons["no"] = Button(
            ig_settings, screen, "images/win_no.png", "否")
        self.buttons["no"].rect.top = self.rect.top + 157
        self.buttons["no"].rect.right = self.rect.right - 77
        self.buttons["no"].image_equal_rect()

    def paste(self):
        """粘贴窗口及按钮"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        for button in self.buttons.values():
            button.paste()
