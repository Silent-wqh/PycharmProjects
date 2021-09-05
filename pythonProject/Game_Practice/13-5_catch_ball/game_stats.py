class GameStats():
    """游戏信息记录"""
    def __init__(self):

        # 游戏活动标志
        self.game_active = True

        # 球到达底部标志
        self.ball_reach_bottom = False

        # 球碰篮子标志
        self.ball_reach_basket = False