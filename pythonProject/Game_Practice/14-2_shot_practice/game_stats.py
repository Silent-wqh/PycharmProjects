class GameStats:
    """游戏信息统计"""

    def __init__(self, settings):

        # 游戏活动开关
        self.game_active = False

        # 飞船生命数
        self.ship_live = 3

        # 未射中次数
        self.not_shot = 0
