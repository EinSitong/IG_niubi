class Settings:
    """游戏设置"""
    
    def __init__(self):
        """初始化游戏设置"""

        # 初始化游戏静态设置

        # screen set
        self.screen_width = 1200
        self.screen_height = 800

        # xiaozhang set
        self.number_limit = 3

        # hot_dog set
        self.hot_dogs_number = 7

        # game speedup_scale
        self.speedup_scale = 1.1
        self.score_scale = 1.1

        # 初始化游戏动态设置

        # xiaozhang set
        self.xiaozhang_speed_factor = 5.5

        # hot_dog set
        self.hot_dog_speed_factor = 8.5

        # dogface set
        self.dogface_set = {'speed': 2.5, 'points': 45, "create n": 5, 'flee n': 2}
        self.dogface_speed = 2.5
        self.dogface_points = 45
        self.dogface_number = 5
        self.flee_number = 2

    def initialize_dynamic_settings(self):
        """初始化游戏动态设置"""

        # xiaozhang set
        self.xiaozhang_speed_factor = 5.5

        # hot_dog set
        self.hot_dog_speed_factor = 10.5

        # dogface set
        self.dogface_speed = 2.5
        self.dogface_points = 45
        self.dogface_number = 5
        self.flee_number = 2

    def increase_speed(self):
        """游戏难度提升"""

        # 难度提升
        self.xiaozhang_speed_factor *= self.speedup_scale
        self.hot_dog_speed_factor *= self.speedup_scale
        self.dogface_speed *= self.speedup_scale

        # 小兵单位分数提升
        self.dogface_points *= self.score_scale
