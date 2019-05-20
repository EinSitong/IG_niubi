import csv


class GameStats:
    """游戏数据与Flag"""

    def __init__(self, ig_settings):
        """初始化数据与Flag"""

        self.ig_settings = ig_settings

        # 游戏数据读取
        with open("game_data/game_data.csv") as f:
            dictreader = csv.DictReader(f)
            game_data = next(dictreader)
            for key, value in game_data.items():
                game_data[key] = int(value)
            self.game_data = game_data

        # 最高分数据读取
        with open("game_data/scores.txt") as file_object:
            scores = [int(score.rstrip()) for score in file_object]
        self.scores = sorted(scores, reverse=True)[0:12]

        # 页面切换flag
        self.game_active = False
        self.zgf_sign = False
        self.game_over = False

        # 子弹方向flag
        self.dogflagxy = True
        self.dogflagzf = True

    def reset_stats(self):
        """重置数据"""
        for key, value in self.game_data.items():
            self.game_data[key] = 0
        self.game_data["xiaozhang_left"] = self.ig_settings.number_limit
