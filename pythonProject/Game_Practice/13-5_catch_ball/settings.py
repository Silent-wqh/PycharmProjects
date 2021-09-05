class Settings:
    """设置"""
    def __init__(self):

        # 屏幕尺寸
        self.screen_width = 1024
        self.screen_height = 768
        # 屏幕颜色
        self.bg_color = (90, 90, 90)

        # 篮子移动速度
        self.basket_speed = 1

        # 球的移动速度
        self.ball_speed = 0.2

        # 可接受失误次数
        self.accept_fail = 3
